from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import Usuario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def index(request):
    return render(request,"preguntas/index.html")

def jugar(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        ...


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
            return redirect('/')
    return render(request,'login',{

        })    