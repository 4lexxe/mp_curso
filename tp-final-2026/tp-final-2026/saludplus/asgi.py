"""Punto de entrada ASGI del proyecto Clínica SaludPlus."""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "saludplus.settings")

application = get_asgi_application()
