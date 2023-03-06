import csv
from datetime import datetime
import pandas as pd

from django.db.models import Q
from django.utils.dateparse import parse_date
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser

from .models import User
from .tasks import process_user_csv
from .serializers import UserSerializer, FileUploadSerializer, FileSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Search by first_name or last_name
        search_query = self.request.query_params.get("search", "")
        if search_query:
            queryset = queryset.filter(
                Q(first_name__icontains=search_query)
                | Q(last_name__icontains=search_query)
            )

        # Search by date range for dob
        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        if start_date and end_date:
            start_date = parse_date(start_date)
            end_date = parse_date(end_date)
            queryset = queryset.filter(birth_date__range=[start_date, end_date])

        # Search by phone_number or email
        phone_number = self.request.query_params.get("phone_number")
        email = self.request.query_params.get("email")
        if phone_number:
            queryset = queryset.filter(phone_number__icontains=phone_number)
        if email:
            queryset = queryset.filter(email__icontains=email)

        # Sort by any field
        sort_by = self.request.query_params.get("sort_by", "id")
        if sort_by:
            queryset = queryset.order_by(sort_by)

        return queryset


class UserUploadAPIView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data["file"]
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            print(row)
            new_file = User(
                first_name=row["first_name"],
                last_name=row["last_name"],
                national_id=row["national_id"],
                birth_date=row["birth_date"],
                address=row["address"],
                country=row["country"],
                phone_number=row["phone_number"],
                email=row["email"],
                finger_print_signature=row["finger_print_signature"],
            )
            new_file.save()
        return Response({"status": "success"}, status.HTTP_201_CREATED)


class FileUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            # Get the file from the serializer
            file_obj = serializer.validated_data["file"]
            timestamp = str(datetime.now().timestamp()).replace(".", "-")
            destination = open("csv/" + timestamp + "-" + file_obj.name, "wb+")
            print(destination)
            for chunk in file_obj.chunks():
                destination.write(chunk)
            destination.close()

            print("Finished--Copying")

            process_user_csv.delay("csv/" + timestamp + "-" + file_obj.name)

            return Response({"status": "success"})
        else:
            return Response(serializer.errors, status=400)


class FileUploadViewing(APIView):
    def get(self, request, format=None):

        return Response({"status": User.objects.count()})
        # return Response({'status': 'success'})
