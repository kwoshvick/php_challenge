from rest_framework import serializers
from .models import User


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
