"""
Mapa de rutas raíz del proyecto Clínica SaludPlus.
Delega las rutas de la aplicación `core` en core.urls.
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
]
