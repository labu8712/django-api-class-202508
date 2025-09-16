#!/bin/sh
set -e

uv run manage.py migrate

uv run manage.py createsuperuser --noinput

uv run manage.py runserver_plus --print-sql 0.0.0.0:8000
