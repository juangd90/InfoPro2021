from django.contrib import admin
from .models import Pregunta, Jugador,PreguntaCategoria
# Register your models here.
admin.site.register(Pregunta)
admin.site.register(Jugador)
admin.site.register(PreguntaCategoria)
