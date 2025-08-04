"""
WSGI config for gabm_infra project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gabm_infra.settings')

application = get_wsgi_application()


# In production, use WhiteNoise to serve static files
if (os.getenv("ENVIRONMENT", "DEV") == "PROD"):
    from whitenoise import WhiteNoise
    STATIC_ROOT = os.getenv("STATIC_ROOT", "/app/static_root")
    application = WhiteNoise(application, root=STATIC_ROOT, autorefresh=True)