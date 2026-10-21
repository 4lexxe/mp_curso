from django.urls import path
from .views import buscar_y_guardar_pokemon

urlpatterns = [
  path('', buscar_y_guardar_pokemon, name='buscar_pokemon'),    
]