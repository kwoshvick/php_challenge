import pandas as pd

from pbp_challenge.celery import app
from django.shortcuts import get_object_or_404
from celery.utils.log import get_task_logger

from user.models import User, UserCsvFile

logger = get_task_logger(__name__)


@app.task()
def process_user_csv(file_id, path):
    file = get_object_or_404(UserCsvFile, pk=file_id)
    file.to_state_inserting()
    file.save()
    try:
        for chunk in pd.read_csv(path, chunksize=1000):
            data = chunk.to_dict(orient="records")
            User.objects.bulk_create([User(**row) for row in data], batch_size=10000)
        file.to_state_processed()
        file.save()
    except Exception as e:
        print("Exception", e)
        file.to_state_failed_from_inserting()
        file.save()
