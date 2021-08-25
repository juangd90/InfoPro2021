from django.contrib import admin
from .models import Pregunta, Jugador, PreguntasRespondidas
# Register your models here.
admin.site.register(Pregunta)
admin.site.register(Jugador)
admin.site.register(PreguntasRespondidas)