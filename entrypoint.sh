#!/usr/bin/env sh

python3 manage.py migrate --no-input
python manage.py createsuperuser --email enricolimanavarro@gmail.com --username admin
python manage.py runserver 0.0.0.0:8000