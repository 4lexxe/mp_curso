from django.shortcuts import render, redirect
# pyrefly: ignore [missing-import]
import requests

from django.contrib import messages
from .models import Pokemon
from .forms import PokemonForm

def buscar_y_guardar_pokemon(request):
    pokemon_api = None
    error_msg = None

    # 1. Si el usuario hace clic en "Guardar en Base de Datos" (POST)
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            poke_id = form.cleaned_data['poke_id']
            # Verificamos si ya existe para no duplicar
            if not Pokemon.objects.filter(poke_id=poke_id).exists():
                form.save()
                messages.success(request, f"¡{form.cleaned_data['nombre']} guardado con éxito en MySQL!")
            else:
                messages.info(request, "Este Pokémon ya está registrado en tu base de datos.")
            return redirect('buscar_pokemon')
        else:
            error_msg = "Error al validar los datos del Pokémon."
    else:
        form = PokemonForm()

    # 2. Búsqueda en PokéAPI vía GET (si pasaron 'nombre')
    query = request.GET.get('nombre', '').strip().lower()
    if query:
        url = f"https://pokeapi.co/api/v2/pokemon/{query}"
        try:
            resp = requests.get(url, timeout=5)
            if resp.status_code == 200:
                data = resp.json()
                pokemon_api = {
                    'poke_id': data['id'],
                    'nombre': data['name'].capitalize(),
                    'imagen': data['sprites']['front_default'],
                    'altura': data['height'] / 10,
                    'peso': data['weight'] / 10,
                    'tipos': ", ".join([t['type']['name'].capitalize() for t in data['types']]),
                }
                # Precargamos el formulario con los datos de la API
                form = PokemonForm(initial=pokemon_api)
            elif resp.status_code == 404:
                error_msg = f"No se encontró el Pokémon '{query}' en PokéAPI."
            else:
                error_msg = "Error al contactar con la API externa."
        except requests.RequestException:
            error_msg = "Error de red al consultar PokéAPI."

    # 3. Traer todos los pokémon guardados en MySQL
    pokemones_guardados = Pokemon.objects.all().order_by('-creado_en')

    context = {
        'pokemon': pokemon_api,
        'form': form,
        'error': error_msg,
        'guardados': pokemones_guardados,
    }
    return render(request, 'pokedex/detalle.html', context)