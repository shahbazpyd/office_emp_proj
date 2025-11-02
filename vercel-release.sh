#!/bin/bash
echo "--- VERCEL RELEASE: START ---"
echo "Running Django database migrations..."
python manage.py migrate --noinput
echo "Django migrations finished."
echo "--- VERCEL RELEASE: END ---"