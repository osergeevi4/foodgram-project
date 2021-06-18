#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata initial_data.json
python manage.py collectstatic --no-input
gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000