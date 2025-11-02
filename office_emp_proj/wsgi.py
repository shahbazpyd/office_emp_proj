# In office_emp_proj/wsgi.py

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise # 💡 NEW: Import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'office_emp_proj.settings')

application = get_wsgi_application()

# 💡 NEW: Wrap the application with WhiteNoise
# This tells WhiteNoise where the collected files are (STATIC_ROOT)
application = WhiteNoise(application) 

# This variable is what Vercel looks for
app = application