#!/bin/bash
echo "migration is happening"
python manage.py migrate
echo "migrations is done"