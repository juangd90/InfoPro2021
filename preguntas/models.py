from django.db import models

# Create your models here.
opciones=(
        ("Politica","Politica"),
        ("Geografica","Geografia"),
        ("Naturaleza","Naturaleza"),
        ("Cultura","Cultura"),
        ("Historia","Historia")
    )

class Pregunta(models.Model):
    
    pregunta=models.CharField(max_length=100)
    respuesta1=models.CharField(max_length=100)
    respuesta2=models.CharField(max_length=100)
    respuesta3=models.CharField(max_length=100)
    respuesta4=models.CharField(max_length=100)
    correcta=models.CharField(max_length=100)
    categoria=models.CharField(max_length=64,choices=opciones,default="Politica")
    dificultad=models.IntegerField(default=1)
    
    def __str__(self):
      return self.pregunta

class Jugador(models.Model):
    nombre=models.CharField(max_length=64)
    apellido=models.CharField(max_length=64)
    puntaje=models.IntegerField(default=0)

    def __str__(self):
        return f"({self.nombre} {self.apellido}) {self.puntaje} "

class Juego(models.Model):
    jugador=Jugador
    preguntas=models.ManyToManyField(Pregunta,blank=True)              