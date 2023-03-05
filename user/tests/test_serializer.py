from django.test import TestCase
from user.models import User
from user.serializers import UserSerializer


class PersonSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            first_name="John",
            last_name="Doe",
            national_id="1234567890",
            birth_date="1990-01-01",
            address="123 Main St, Anytown, USA",
            country="United States",
            phone_number="555-555-1234",
            email="john.doe@example.com",
            finger_print_signature="ABCDEF123456",
        )

    def test_person_serializer(self):
        serializer = UserSerializer(instance=self.user)
        self.assertEqual(serializer.data["id"], 1)
        self.assertEqual(serializer.data["first_name"], "John")
        self.assertEqual(serializer.data["last_name"], "Doe")
        self.assertEqual(serializer.data["national_id"], 1234567890)
        self.assertEqual(serializer.data["birth_date"], "1990-01-01")
        self.assertEqual(serializer.data["address"], "123 Main St, Anytown, USA")
        self.assertEqual(serializer.data["country"], "United States")
        self.assertEqual(serializer.data["phone_number"], "555-555-1234")
        self.assertEqual(serializer.data["email"], "john.doe@example.com")
        self.assertEqual(serializer.data["finger_print_signature"], "ABCDEF123456")

    def test_count_person_serializer_field(self):
        serializer = UserSerializer(instance=self.user)
        self.assertEqual(10, len(serializer.fields.keys()))
