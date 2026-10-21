from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['poke_id', 'nombre', 'imagen', 'altura', 'peso', 'tipos']
        # Los campos se recibirán como datos ocultos para que el usuario no tenga que rellenarlos a mano
        widgets = {
            'poke_id': forms.HiddenInput(),
            'nombre': forms.HiddenInput(),
            'imagen': forms.HiddenInput(),
            'altura': forms.HiddenInput(),
            'peso': forms.HiddenInput(),
            'tipos': forms.HiddenInput(),
        }