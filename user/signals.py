from django.db.models.signals import post_save
from django.dispatch import receiver

from pbp_challenge import settings
from .models import UserCsvFile
from .tasks import process_user_csv


@receiver(post_save, sender=UserCsvFile)
def on_successful_finish_upload(sender, instance, created, **kwargs):
    if not created:
        if instance.state == "pending":
            process_user_csv.delay(instance.id, settings.MEDIA_ROOT + instance.name)
