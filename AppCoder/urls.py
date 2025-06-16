from django.urls import path
from .views import lista_estudiantes, detalle_estudiante, cursos, profesores, estudiantes, entregables,inicio
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    # path('estudiantes/', lista_estudiantes, name="lista_estudiantes"),
    # path('estudiantes/<int:pk>/', detalle_estudiantes, name="detalle_estudiantes"),
    path("", inicio, name="inicio"),
    path("cursos/", cursos, name="cursos"),
    path("profesores/", profesores, name="profesores"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("entregables/", entregables, name="entregables"),
    
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
