#!/bin/sh
set -e

uv run manage.py migrate

if uv run manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); exit(0 if User.objects.filter(is_superuser=True).exists() else 1)"; then
    echo "Superuser already exists"
else
    uv run manage.py createsuperuser --noinput
fi

uv run manage.py runserver_plus --print-sql 0.0.0.0:8000
