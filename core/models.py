from django.db import models


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Estudiante(models.Model): 
    nombre = models.CharField(max_length=100) 
    apellido = models.CharField(max_length=100) 
    email = models.EmailField() 
    def __str__(self): 
        return f"{self.nombre} {self.apellido}"
    
class Profesor(models.Model): 
    nombre = models.CharField(max_length=100) 
    apellido = models.CharField(max_length=100) 
    email = models.EmailField() 
    profesion = models.CharField(max_length=100) 
    def __str__(self): 
        return f"{self.nombre} {self.apellido} - {self.profesion}"
    
class Curso(models.Model): 
    nombre = models.CharField(max_length=100) 
    camada = models.IntegerField() 
    def __str__(self): 
        return self.nombre 

class Entregable(models.Model): 
    nombre = models.CharField(max_length=100) 
    fecha_entrega = models.DateField() 
    entregado = models.BooleanField() 
    def __str__(self): 
        return self.nombre


# Create your models here.
