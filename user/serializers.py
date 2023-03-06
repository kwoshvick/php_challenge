from rest_framework import serializers
from .models import User
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
        ]


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    def validate(self, attrs):
        file = attrs.get("file")
        if not file:
            raise serializers.ValidationError(_("No file uploaded."))
        if not file.name.endswith(".csv"):
            raise serializers.ValidationError(_("Invalid file format."))
        return attrs


class FileSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ("file",)

    def validate(self, attrs):
        file = attrs.get("file")
        if not file:
            raise serializers.ValidationError(_("No file uploaded."))
        if not file.name.endswith(".csv"):
            raise serializers.ValidationError(_("Invalid file format."))
        return attrs
