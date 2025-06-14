from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludar(request):
    return HttpResponse("Hola desde Django")

def index(request):
    return render(request, 'core/index.html')

def saludar_con_etiqueta(request):
    return HttpResponse('<h1 style="color:red"> Hola </h1>')

def saludar_con_parametros(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.upper()
    return HttpResponse(f"{apellido}, {nombre}")


