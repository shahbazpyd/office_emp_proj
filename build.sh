# In build.sh (Alternative - Try this if the first one doesn't work)
#!/bin/bash

# 1. Install dependencies (ensure they are installed in a location the shell can find)
pip install -r requirements.txt

# 2. Use the shell's python
python manage.py migrate --noinput
python manage.py collectstatic --noinput --clear