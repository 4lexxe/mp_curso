from django.contrib import admin
from .models import Pokemon

# Register your models here.
@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('poke_id', 'nombre', 'tipos', 'altura', 'peso', 'creado_en')
    search_fields = ('nombre', 'poke_id')