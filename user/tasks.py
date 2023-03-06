import pandas as pd

from pbp_challenge.celery import app
from celery.utils.log import get_task_logger

from user.models import User

logger = get_task_logger(__name__)


@app.task()
def process_user_csv(path):
    for chunk in pd.read_csv(path, chunksize=1000):
        data = chunk.to_dict(orient="records")
        User.objects.bulk_create(
            [User(**row) for row in data],
            # batch_size=10000
        )
        print("Batch inserted----------------------------------")

    print("Done -----")
