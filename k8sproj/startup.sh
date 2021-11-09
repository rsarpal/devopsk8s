#!/bin/bash
set -e

echo "START Running Django on `date`"
python3 manage.py runserver 0.0.0.0:8000