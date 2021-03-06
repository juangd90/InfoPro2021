from django.contrib.messages.api import MessageFailure
from preguntas.models import Pregunta,Jugador,PreguntaCategoria
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import Usuario
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.contrib import messages
# Create your views here.
@login_required(login_url='login/')
def index(request):   
    jugador,created=Jugador.objects.get_or_create(nombre=request.user)
    jugador.resetearPuntaje()
    return render(request,'preguntas/index.html')

def jugar(request,dificultad,orden):
    if not request.user.is_authenticated: #controla que este logueado el usuario, sino lo manda al login
        return redirect('login')
    else:       
        
        #aca va la logica del juego, por ej mandar al usuario las preguntas, y preguntar si desea continuar o quiere salir del juego. En cualquier caso se debe calcular el puntaje y mostrar por pantalla. Para manejar las preguntas se podria utilizar un for
        
        jugador,created=Jugador.objects.get_or_create(nombre=request.user)
        
        if request.method=='POST': 
            #filtra solamente las preguntas con la dificuultad que recibe como parametro           
            preguntas=Pregunta.objects.filter(dificultad=dificultad,orden=orden)
            contador=orden+1
            puntaje=0
            respuesta=None
            correcta=None
            for p in preguntas:                
                if p.correcta==request.POST.get(p.pregunta):
                    respuesta=request.POST.get(p.pregunta)
                    puntaje=puntaje+p.dificultad                   
                    
                   
                else:
                    correcta=p.correcta                
            jugador.acumularPuntaje(puntaje)            
            puntaje_juego=jugador.puntaje
            jugador.calcularPuntaje(jugador.puntaje)
            puntaje_total=jugador.puntaje_maximo
            #puntaje_total=jugador.puntaje    
            contexto={
                'puntaje':puntaje,
                'correcta':correcta,
                'respuesta':respuesta,                
                'contador':contador,
                'nivel':dificultad,
                'puntaje_juego':puntaje_juego,
                'puntaje_total':puntaje_total
                
            }
            
            return render(request,'preguntas/resultados.html',contexto)
        else:
            
            preguntas=Pregunta.objects.all()
            return render(request,'preguntas/jugar.html',{
                
                'preguntas':preguntas,
                'nivel':dificultad,
                'orden':orden,               
            })                 


def jugarCategoria(request,categoria,orden):
    if not request.user.is_authenticated: #controla que este logueado el usuario, sino lo manda al login
        return redirect('login')
    else:       
        
        #aca va la logica del juego, por ej mandar al usuario las preguntas, y preguntar si desea continuar o quiere salir del juego. En cualquier caso se debe calcular el puntaje y mostrar por pantalla. Para manejar las preguntas se podria utilizar un for
        
        jugador,created=Jugador.objects.get_or_create(nombre=request.user)
        
        if request.method=='POST': 
            #filtra solamente las preguntas con la dificuultad que recibe como parametro           
            preguntas=PreguntaCategoria.objects.filter(categoria=categoria,orden=orden)
            contador=orden+1
            puntaje=0
            respuesta=None
            correcta=None
            for p in preguntas:                
                if p.correcta==request.POST.get(p.pregunta):
                    respuesta=request.POST.get(p.pregunta)
                    puntaje=puntaje+p.dificultad                   
                    
                   
                else:
                    correcta=p.correcta                
            jugador.acumularPuntaje(puntaje)            
            puntaje_juego=jugador.puntaje
            jugador.calcularPuntaje(jugador.puntaje)
            puntaje_total=jugador.puntaje_maximo
            #puntaje_total=jugador.puntaje    
            contexto={
                'puntaje':puntaje,
                'correcta':correcta,
                'respuesta':respuesta,                
                'contador':contador,
                'categoria':categoria,
                'puntaje_juego':puntaje_juego,
                'puntaje_total':puntaje_total
                
            }
            
            return render(request,'preguntas/resultados_categoria.html',contexto)
        else:
            
            preguntas=PreguntaCategoria.objects.all()
            return render(request,'preguntas/jugar_categoria.html',{
                
                'preguntas':preguntas,
                'categoria':categoria.title(),
                'orden':orden,               
            })

def registro(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method=='POST':
        form=Usuario(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))

        messages.error(request, "Error en el registro, por favor verifique los datos ingresados")  
        
    form=Usuario()
    return render(request,'preguntas/registro.html',{
                'form':form
            })    
        
def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        usuario=authenticate(request,username=username,password=password)
        
        if usuario is not None:
            login(request,usuario)
            
            return HttpResponseRedirect('/')
        else:
            messages.error(request,"Error de usuario o contrase??a")    
    return render(request,'preguntas/login.html',{

        })

def logout_user(request):
    logout(request)
    return redirect('index')   

def tablero(request):
    total_usuarios=Jugador.objects.order_by('-puntaje_maximo')[:10]
    contador=total_usuarios.count()
    return render(request,'preguntas/tablero.html',{
        'total_usuarios':total_usuarios,
        'contador':contador,
    })

def handler500(request):
    return render(request,'preguntas/index.html')             