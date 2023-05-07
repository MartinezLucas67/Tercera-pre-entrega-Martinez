from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=64) #equivalente a str
    comision = models.IntegerField() #equivalente a int
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    fecha_nacimiento = models.DateField
    dni = models.CharField(max_length=32)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    

class Profesor(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    fecha_nacimiento = models.DateField
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    biografia = models.TextField()

class Entrega(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_entrega = models.DateTimeField()
    esta_aprobado = models.BooleanField(default=False)

 