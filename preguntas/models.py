from django.db import models
from django.db.models.fields import BooleanField

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
    orden=models.IntegerField(default=1)
     
        
    
    def __str__(self):
      return f"({self.pregunta}- {self.dificultad})"

class Jugador(models.Model):
    nombre=models.CharField(max_length=64)
    apellido=models.CharField(max_length=64)
    puntaje=models.IntegerField(default=0)

    def calcularPuntaje(self,puntaje):
        if puntaje>self.puntaje:
            self.puntaje=puntaje
            self.save()

    

    

    def __str__(self):
        return f"({self.nombre} {self.apellido}) {self.puntaje} "
#probar reemplazar por preguntas respondidas
class PreguntasRespondidas(models.Model):
    jugador=models.ForeignKey(Jugador,on_delete=models.CASCADE)
    preguntas=models.ForeignKey(Pregunta,blank=True,on_delete=models.CASCADE,default=None) 
    puntaje_obtenido=models.DecimalField(default=0,decimal_places=2,max_digits=6)             

   #en la clase pregunta solamente lo relacionado a las preguntas
   #con la clase jugador podemos manejar la info basica del mismo, y guardar su puntaje
   # Hay que analizar si es necesaria la clase juego 