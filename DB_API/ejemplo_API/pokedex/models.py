from django.db import models

# Create your models here.
class Pokemon(models.Model):
    poke_id = models.IntegerField(unique=True, verbose_name="ID PokéAPI")
    nombre = models.CharField(max_length=100)
    imagen = models.URLField(max_length=300)
    altura = models.FloatField(help_text="En metros")
    peso = models.FloatField(help_text="En kilogramos")
    tipos = models.CharField(max_length=100, help_text="Tipos separados por coma")
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"#{self.poke_id} {self.nombre}"