from django.urls import path
from .views import lista_estudiantes, detalle_estudiante, busqueda_camada, buscar, busquedaCamada, profesorFormulario, cursos, cursoFormulario2, cursoFormulario, profesores, estudiantes, entregables,inicio, App
from django.conf.urls.static import static
from django.conf import settings
from .import views



urlpatterns = [
    # path('estudiantes/', lista_estudiantes, name="lista_estudiantes"),
    # path('estudiantes/<int:pk>/', detalle_estudiantes, name="detalle_estudiantes"),
    path("", inicio, name="inicio"),
    path("App/", App, name= "App"),
    path("cursos/", cursos, name="cursos"),
    path("profesores/", profesores, name="profesores"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("entregables/", entregables, name="entregables"),
    path("cursoFormulario/", cursoFormulario, name="cursoFormulario"),
    path("cursoFormulario2/", cursoFormulario2, name="cursoFormulario2"),
    path("profesorFormulario/", profesorFormulario, name="profesorFormulario"),
    # path('busquedaCamada', busquedaCamada, name="busquedaCamada"),
    # path('buscar/', buscar, name='buscar'),
    path('cursos/busqueda/', views.busqueda_camada, name='busquedaCamada'),

    
    
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
