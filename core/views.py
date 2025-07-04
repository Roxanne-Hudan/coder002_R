from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


# Create your views here.

def saludar(request):
    return HttpResponse("Hola desde Django")

#def probandoTemplate(self):
#    nombre ="Rox"
#    apellido = "colosia"
#    notas = [10, 2, 4, 7, 3]
#    notas_malas = [6, 4, 2]
#
#    dicionario = {
#        "nombre": nombre,
#        "apellido": apellido,
#        "notas": notas,
#        "notas_malas": notas_malas,
#    }

def index(request):
    posts = Post.objects.all()  # obtenemos todos los posts
    return render(request, 'core/index.html', {'posts': posts})

#def index(request):
#    return render(request, 'core/index.html')
#

def index2(request):
    posts = Post.objects.all()  # ← posts en plural
    return render(request, 'AppBlog/index.html', {'posts': posts}) 

def saludar_con_etiqueta(request):
    return HttpResponse('<h1 style="color:red"> Hola </h1>')

def saludar_con_parametros(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.upper()
    return HttpResponse(f"{apellido}, {nombre}")

def blog(request):
    posts = Post.objects.all()  # obtenemos todos los posts
    return render(request, 'core/base.html', {'posts': posts})
