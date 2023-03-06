from rest_framework import serializers
from .models import User, UserCsvFile
from django.utils.translation import gettext_lazy as _


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "national_id",
            "birth_date",
            "address",
            "country",
            "phone_number",
            "email",
            "finger_print_signature",
            "created_at",
            "updated_at",
        ]


class UserCsvFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCsvFile
        fields = ["id", "state", "name", "original_name", "created_at", "updated_at"]


class FileSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ("file",)

    def validate(self, attrs):
        file = attrs.get("file")
        if not file:
            raise serializers.ValidationError("No file uploaded.")
        if not file.name.endswith(".csv"):
            raise serializers.ValidationError("Invalid file format.")
        return attrs
