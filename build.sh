# In build.sh (make sure you rename build_files.sh to build.sh)
#!/bin/bash

# 1. Install dependencies
pip install -r requirements.txt

# 2. Run database migrations (optional, but good)
python manage.py migrate --noinput

# 3. Collect static files into the STATIC_ROOT directory defined in settings.py
python manage.py collectstatic --noinput --clear

echo "Build finished. Static files collected."