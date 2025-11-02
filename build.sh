# In build.sh (Updated)
#!/bin/bash

# Vercel's Python path is needed explicitly in the build step
PYTHON_EXEC="$PYTHONUSERBASE/bin/python"

# 1. Install dependencies
# Use the Python executable's pip
$PYTHON_EXEC -m pip install -r requirements.txt

# 2. Run database migrations
$PYTHON_EXEC manage.py migrate --noinput

# 3. Collect static files
$PYTHON_EXEC manage.py collectstatic --noinput --clear

echo "Build finished. Static files collected."