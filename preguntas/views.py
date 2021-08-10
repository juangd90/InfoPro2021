from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import Usuario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect

# Create your views here.
#@login_required()
def index(request):
    return render(request,"preguntas/index.html")

def jugar(request):
    if not request.user.is_authenticated: #controla que este logueado el usuario, sino lo manda al login
        return redirect('login')
    else:
        ...
        #aca va la logica del juego, por ej mandar al usuario 4 preguntas, y preguntar si desea continuar o quiere salir del juego. En cualquier caso se debe calcular el puntaje y mostrar por pantalla. Para manejar las preguntas se podria utilizar un for y asi buscar de a 4 preguntas en la BD



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
        
def login(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        usuario=authenticate(request,username=username,password=password)
        if usuario is not None:
            login(request,usuario)
            return HttpResponseRedirect('/')
    return render(request,'preguntas/login.html',{

        })      