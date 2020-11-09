#!/usr/bin/env sh

# waiting postgress
sleep 30

# run migrations
python3 manage.py migrate --no-input >> /tmp/migrate_result

# start server
python3 manage.py runserver 0.0.0.0:80