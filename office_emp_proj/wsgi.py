# In office_emp_proj/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'office_emp_proj.settings')

application = get_wsgi_application()

# Vercel needs this 'app' variable
app = application