from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index_html'),
    path('acercade/', views.acercade, name='acercade'),
    path('acercade.html', views.acercade, name='acercade_html'),
    path('contacto/', views.contacto, name='contacto'),
    path('contacto.html', views.contacto, name='contacto_html'),
    path('productos/', views.productos, name='productos'),
    path('productos.html', views.productos, name='productos_html'),
]
