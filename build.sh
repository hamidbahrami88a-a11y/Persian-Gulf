#!/usr/bin/env bash
set -o errexit
pip install -r requirements.tex
python manage.py migrate
python manage.py createsuperuser --noinput
python manage.py collectstatic --noinput