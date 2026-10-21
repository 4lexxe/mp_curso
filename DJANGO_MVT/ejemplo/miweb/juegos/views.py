from django.shortcuts import render
from .models import videojuegos

# Create your views here.

def inicio(request):
    return render(request, "juegos/index.html", {"videojuegos": videojuegos})

