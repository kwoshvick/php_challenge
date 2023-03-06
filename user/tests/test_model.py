from django.test import TestCase
from user.models import User, UserCsvFile


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


class UserCsvFileTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.file = UserCsvFile.objects.create(
            name="234fg-gg.csv",
            original_name="gg.csv",
        )

    def test_user_csv_file_count(self):
        self.assertEqual(1, UserCsvFile.objects.count())

    def test_default_state(self):
        self.assertEqual("uploading", self.file.state)

    def test_change_state_to_failed_from_uploading(self):
        self.file.to_state_failed_from_uploading()
        self.file.save()
        self.assertEqual("failed", self.file.state)

    def test_change_state_to_pending(self):
        self.file.to_state_pending()
        self.file.save()
        self.assertEqual("pending", self.file.state)

    def test_change_state_to_inserting(self):
        self.file.to_state_pending()
        self.file.to_state_inserting()
        self.file.save()
        self.assertEqual("inserting", self.file.state)

    def test_change_state_to_failed_from_inserting(self):
        self.file.to_state_pending()
        self.file.to_state_inserting()
        self.file.to_state_failed_from_inserting()
        self.file.save()
        self.assertEqual("failed", self.file.state)

    def test_change_state_to_processed(self):
        self.file.to_state_pending()
        self.file.to_state_inserting()
        self.file.to_state_processed()
        self.file.save()
        self.assertEqual("processed", self.file.state)
