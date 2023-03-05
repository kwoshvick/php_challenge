from django.test import TestCase
from user.models import User
from user.serializers import UserSerializer


class PersonSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            first_name="Victor",
            last_name="Lwanga",
            national_id=1234567890,
            birth_date="1990-01-01",
            address="UpperHill, Raptor Road",
            country="Kenya",
            phone_number="555-555-1234",
            email="victor.lwanga@ymail.com",
            finger_print_signature="ABCD4566#!@#$%EF123456",
        )

    def test_person_serializer(self):
        serializer = UserSerializer(instance=self.user)
        self.assertEqual(serializer.data["id"], 1)
        self.assertEqual(serializer.data["first_name"], "Victor")
        self.assertEqual(serializer.data["last_name"], "Lwanga")
        self.assertEqual(serializer.data["national_id"], 1234567890)
        self.assertEqual(serializer.data["birth_date"], "1990-01-01")
        self.assertEqual(serializer.data["address"], "UpperHill, Raptor Road")
        self.assertEqual(serializer.data["country"], "Kenya")
        self.assertEqual(serializer.data["phone_number"], "555-555-1234")
        self.assertEqual(serializer.data["email"], "victor.lwanga@ymail.com")
        self.assertEqual(
            serializer.data["finger_print_signature"], "ABCD4566#!@#$%EF123456"
        )

    def test_count_person_serializer_field(self):
        serializer = UserSerializer(instance=self.user)
        self.assertEqual(10, len(serializer.fields.keys()))
