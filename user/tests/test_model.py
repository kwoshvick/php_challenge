from django.test import TestCase
from user.models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(
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

    def test_user_count(self):
        self.assertEqual(1, User.objects.count())
