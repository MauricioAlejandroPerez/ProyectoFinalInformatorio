"""
WSGI config for ProyectoFinalInfo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# from whitenoise import Whitenoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoFinalInfo.settings.local')

application = get_wsgi_application()
# application = Whitenoise(application)
