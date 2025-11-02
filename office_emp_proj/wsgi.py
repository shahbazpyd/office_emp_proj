# In office_emp_proj/wsgi.py

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise 
from django.conf import settings # 💡 NEW: Import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'office_emp_proj.settings')

application = get_wsgi_application()

# 💡 FIX: Wrap with WhiteNoise, explicitly setting the root to STATIC_ROOT
# WhiteNoise will now look exactly where collectstatic put the files.
application = WhiteNoise(application, root=settings.STATIC_ROOT)

# Vercel needs this 'app' variable
app = application