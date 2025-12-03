#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "Starting database migration..."
python manage.py migrate
echo "Database migration completed successfully."
