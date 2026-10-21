"""
Mapa de rutas estáticas del Sprint 1 - Clínica SaludPlus.

Rutas:
    /                 -> Inicio (Home)
    /especialidades/  -> Especialidades Médicas
    /profesionales/   -> Staff Profesional
    /reservar/        -> Gestión de Turnos
    /contacto/        -> Contacto e Institucional
"""
from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.InicioView.as_view(), name="inicio"),
    path("especialidades/", views.EspecialidadesView.as_view(), name="especialidades"),
    path("profesionales/", views.ProfesionalesView.as_view(), name="profesionales"),
    path("reservar/", views.ReservarView.as_view(), name="reservar"),
    path("contacto/", views.ContactoView.as_view(), name="contacto"),
]
