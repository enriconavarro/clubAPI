#!/usr/bin/env sh

python3 manage.py migrate --no-input >> /tmp/migrate_result
python3 manage.py runserver 0.0.0.0:80