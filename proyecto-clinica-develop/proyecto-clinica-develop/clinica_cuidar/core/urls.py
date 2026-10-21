from .views import profesionales
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("reservar",views.reservar, name="reservar"),
    path("contacto",views.contacto, name="contacto"),
    path("especialidades",views.especialidades, name="especialidades"),
    path("profesionales",profesionales, name="profesionales")
]