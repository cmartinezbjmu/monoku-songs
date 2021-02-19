#!/bin/sh

set -e

# Migrate database
python manage.py migrate

# Load data
python manage.py loaddata artist_fixtures
python manage.py loaddata band_fixtures
python manage.py loaddata album_fixtures
python manage.py loaddata genre_fixtures
python manage.py loaddata subgenre_fixtures
python manage.py loaddata similar_band_fixtures
python manage.py loaddata song_fixtures

# Start Django app
python manage.py runserver 0.0.0.0:8000
