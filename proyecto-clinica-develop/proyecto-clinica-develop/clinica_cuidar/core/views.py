from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request,"core/home.html")


def reservar(request):
  return render(request,"core/reservar.html")

def contacto(request):
  return render(request, "core/contacto.html")

def especialidades(request):
  return render(request, "core/especialidades.html")

def profesionales(request):
  return render(request, "core/profesionales.html")
