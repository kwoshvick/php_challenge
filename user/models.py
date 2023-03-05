from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    national_id = models.IntegerField(null=False, blank=False)
    birth_date = models.DateField(null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    country = models.CharField(max_length=30, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=30, null=False, blank=False)
    finger_print_signature = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


class UserCsvFile(models.Model):
    file = models.FileField(blank=False, null=False, upload_to="csv/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
