from preguntas.models import Pregunta
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import Usuario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect

# Create your views here.
@login_required(login_url='login')
def index(request):
    if request.method=='POST':
        nivel=request.POST.get('Dificultad')
        return render(request,"preguntas/jugar.html",{
           'nivel':nivel,
           
        })
    else:
        return render(request,'preguntas/index.html')
def jugar(request):
    if not request.user.is_authenticated: #controla que este logueado el usuario, sino lo manda al login
        return redirect('login')
    
        
        #aca va la logica del juego, por ej mandar al usuario las preguntas, y preguntar si desea continuar o quiere salir del juego. En cualquier caso se debe calcular el puntaje y mostrar por pantalla. Para manejar las preguntas se podria utilizar un for
    else:
        if request.method=='POST':
            preguntas=Pregunta.objects.all()
            puntaje=0
            correcta=0
            incorrecta=0
            for p in preguntas:
                if p.correcta==request.POST.get(p.pregunta):
                    correcta+=1
                    puntaje=puntaje+p.dificultad
                else:
                    incorrecta+=1
            contexto={
                'puntaje':puntaje,
                'correcta':correcta,
                'incorrecta':incorrecta
            }
            return render(request,'preguntas/resultados.html',contexto)
        else:
            preguntas=Pregunta.objects.all()
            return render(request,'preguntas/jugar.html',{
                'preguntas':preguntas
            })                 


def registro(request):
    if request.method=='POST':
        form=Usuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    form=Usuario()
    return render(request,'preguntas/registro.html',{
                'form':form
            })    
        
def login_user(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        usuario=authenticate(request,username=username,password=password)
        if usuario is not None:
            login(request,usuario)
            return HttpResponseRedirect('/')
    return render(request,'preguntas/login.html',{

        })      