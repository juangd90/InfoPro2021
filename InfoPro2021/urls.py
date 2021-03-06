"""InfoPro2021 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from preguntas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    path("registro",views.registro,name="registro"),
    path("login/",views.login_user,name="login"),
    path('jugar/<int:dificultad>/<int:orden>/',views.jugar,name="jugar"),
    path('jugar_categoria/<str:categoria>/<int:orden>/',views.jugarCategoria,name="jugar_categoria"),
    path('loguout_user',views.logout_user,name="logout_user"),
    path('tablero/',views.tablero,name="tablero")

]
handler500='preguntas.views.handler500'