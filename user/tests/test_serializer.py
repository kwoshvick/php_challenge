from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.exceptions import ValidationError
from rest_framework.test import APITestCase
from user.models import User, UserCsvFile
from user.serializers import UserSerializer, UserCsvFileSerializer, FileSerializer


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


class UserCsvFileSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.file = UserCsvFile.objects.create(
            name="234fg-gg.csv",
            original_name="gg.csv",
        )

    def test_count_person_serializer_field(self):
        serializer = UserCsvFileSerializer(instance=self.file)
        self.assertEqual(6, len(serializer.fields.keys()))


class FileSerializerTestCase(APITestCase):
    def test_valid_file(self):
        content = b"foo,bar\n1,2\n3,4\n"
        file = SimpleUploadedFile("test.csv", content, content_type="text/csv")
        serializer = FileSerializer(data={"file": file})
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["file"], file)

    def test_missing_file(self):
        serializer = FileSerializer(data={})
        with self.assertRaises(ValidationError) as cm:
            serializer.is_valid(raise_exception=True)
        self.assertEqual(str(cm.exception.status_code), "400")

    def test_invalid_file_format(self):
        content = b"foo,bar\n1,2\n3,4\n"
        file = SimpleUploadedFile("test.txt", content, content_type="text/plain")
        serializer = FileSerializer(data={"file": file})
        with self.assertRaises(ValidationError) as cm:
            serializer.is_valid(raise_exception=True)
        self.assertEqual(str(cm.exception.status_code), "400")
