#!/bin/sh

set -e

# Migrate database
python manage.py migrate

# Start Django app
python manage.py runserver 127.0.0.1:8000
