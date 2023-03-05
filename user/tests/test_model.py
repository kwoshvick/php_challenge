from django.test import TestCase
from user.models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
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

    def test_user_count(self):
        self.assertEqual(1, User.objects.count())
