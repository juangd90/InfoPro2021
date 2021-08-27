from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.
opciones=(
        ("Politica","Politica"),
        ("Geografia","Geografia"),
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
    orden=models.IntegerField(default=1)
     
        
    
    def __str__(self):
      return f"({self.pregunta}- {self.dificultad})"

class PreguntaCategoria(models.Model):
    pregunta=models.CharField(max_length=100)
    respuesta1=models.CharField(max_length=100)
    respuesta2=models.CharField(max_length=100)
    respuesta3=models.CharField(max_length=100)
    respuesta4=models.CharField(max_length=100)
    correcta=models.CharField(max_length=100)
    categoria=models.CharField(max_length=64,choices=opciones,default="Politica")
    dificultad=models.IntegerField(default=1)
    orden=models.IntegerField(default=1)

    def copiarPregunta(self,pregunta):
        self.pregunta=pregunta
        self.save()

    def __str__(self):
      return f"({self.pregunta}- {self.categoria}-{self.orden})"

      
class Jugador(models.Model):
    nombre=models.CharField(max_length=64)
    apellido=models.CharField(max_length=64)
    puntaje=models.IntegerField(default=0)
    puntaje_maximo=models.IntegerField(default=0)

    def calcularPuntaje(self,puntaje):
        if puntaje>self.puntaje_maximo:
            self.puntaje_maximo=puntaje
            self.save()
    def acumularPuntaje(self,puntaje):
        self.puntaje+=puntaje
        self.save()
    
    def resetearPuntaje(self):
        self.puntaje=0
        self.save()

    

    def __str__(self):
        return f"({self.nombre} {self.apellido}) {self.puntaje} "

   #en la clase pregunta solamente lo relacionado a las preguntas
   #con la clase jugador podemos manejar la info basica del mismo, y guardar su puntaje
   # Hay que analizar si es necesaria la clase juego 