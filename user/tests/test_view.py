from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from user.models import User


class UserListTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.person1 = User.objects.create(
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
        self.person2 = User.objects.create(
            first_name="Jane",
            last_name="Lwanga",
            national_id="0987654321",
            birth_date="1995-01-01",
            address="456 Main St",
            country="US",
            phone_number="0701555100",
            email="jane@example.com",
            finger_print_signature="def456",
        )

    def test_search_by_first_name(self):
        url = reverse("user-list")
        response = self.client.get(url, {"search": "Victor"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], self.person1.id)

    def test_search_by_last_name(self):
        url = reverse("user-list")
        response = self.client.get(url, {"search": "Lwanga"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_search_by_dob_range(self):
        url = reverse("user-list")
        response = self.client.get(
            url, {"start_date": "1990-01-01", "end_date": "1995-01-01"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_search_by_phone_number(self):
        url = reverse("user-list")
        response = self.client.get(url, {"phone_number": "555"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_search_by_exact_phone_number(self):
        url = reverse("user-list")
        response = self.client.get(url, {"phone_number": "0701555100"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_by_email_suffix(self):
        url = reverse("user-list")
        response = self.client.get(url, {"email": ".com"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_search_by_email_domain(self):
        url = reverse("user-list")
        response = self.client.get(url, {"email": "example.com"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_sort_by_first_name(self):
        url = reverse("user-list")
        response = self.client.get(url, {"sort_by": "first_name"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["first_name"], "Jane")
        self.assertEqual(response.data[1]["first_name"], "Victor")

    def test_sort_by_dob(self):
        url = reverse("user-list")
        response = self.client.get(url, {"sort_by": "birth_date"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["id"], self.person1.id)
        self.assertEqual(response.data[1]["id"], self.person2.id)
