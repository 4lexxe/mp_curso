"""Punto de entrada WSGI del proyecto Clínica SaludPlus."""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "saludplus.settings")

application = get_wsgi_application()
