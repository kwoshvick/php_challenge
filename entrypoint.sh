#!/bin/sh
if "$DATABASE" = "pbp_challenge_db"
then
    echo "Waiting for postgres..."
    echo "Host: $SQL_HOST Port: $SQL_PORT"
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.5
    done
    echo "PostgreSQL started"
fi
#SERVER_URL=192.168.0.68
#APP_NAME=oz

# python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input --clear
python manage.py createcachetable
python manage.py shell -c "
from django.contrib.auth import get_user_model;
try:
  get_user_model().objects.filter(email='admin@admin.com').exists() or get_user_model().objects.create_superuser(email='admin@admin.com',password='gateway', username='admin',first_name='admin',last_name='Admin')
except Exception as e:
  print(e)
  "

exec "$@"
