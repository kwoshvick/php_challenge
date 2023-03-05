from django.db.models import Q
from django.utils.dateparse import parse_date
from rest_framework import generics
from .models import User
from .serializers import UserSerializer


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
