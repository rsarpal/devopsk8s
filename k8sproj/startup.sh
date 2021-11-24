#!/bin/bash
set -e

echo "START Running Django on `date`"
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000