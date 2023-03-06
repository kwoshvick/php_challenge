from django.db import models
from django_fsm import FSMField, transition


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
    id = models.AutoField(primary_key=True)
    state = FSMField(default="uploading", protected=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    original_name = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.state}"

    @transition(field=state, source="uploading", target="pending")
    def to_state_pending(self):
        return "File state changed to pending"

    @transition(field=state, source="uploading", target="failed")
    def to_state_failed_from_uploading(self):
        return "File state changed to failed"

    @transition(field=state, source="pending", target="inserting")
    def to_state_inserting(self):
        return "File state changed to inserting"

    @transition(field=state, source="inserting", target="failed")
    def to_state_failed_from_inserting(self):
        return "File state changed to failed"

    @transition(field=state, source="inserting", target="processed")
    def to_state_processed(self):
        return "File state changed to processed"
