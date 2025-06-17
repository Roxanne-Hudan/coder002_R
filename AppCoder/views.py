from django.shortcuts import render, get_object_or_404
from .models import Estudiante, Profesor, Curso, Entregable
from .forms import CursoFormulario, ProfesorFormulario

# Create your views here.

def lista_estudiantes(requets):
    estudiantes = Estudiante.objects.all()
    return render(requets, "estudiantes_list.html", {"estudiantes":estudiantes})

def detalle_estudiante(requets, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(requets, "estudiante_detail.html", {"estudiante":estudiante})

def inicio(request):
    return render(request, "AppCoder/index.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def App(request):
    return render(request, "AppCoder/App.html")

# def cursoFormulario(request):
#     return render(request, "AppCoder/formulario/cursoFormulario.html")

def cursoFormulario(request):
    if request.method == "POST":
        curso = Curso(nombre=request.POST["curso"],camada=(request.POST["camada"]))
        curso.save()
        return render(request, "AppCoder/index.html")
    return render(request, "AppCoder/formulario/cursoFormulario.html")

def cursoFormulario2(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"],camada=informacion["camada"])
            curso.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = CursoFormulario()        
    
    return render(request, "AppCoder/formulario/cursoFormulario2.html", {"miFormulario": miFormulario})


def profesorFormulario(request):

    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)  # aquí llega toda la información del html
        if miFormulario.is_valid():  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            profesor = Profesor(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                email=informacion['email'],
                profesion=informacion['profesion']
            )
            profesor.save()
            return render(request, "AppCoder/index.html")  # Vuelvo al inicio o a donde quieran
    else:
        miFormulario = ProfesorFormulario()  # Formulario vacío para construir el html

    return render(request, "AppCoder/formulario/profesorFormulario.html", {"miFormulario": miFormulario})