from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=64) #equivalente a str
    comision = models.IntegerField() #equivalente a int
    
    def __str__(self):
        return f"{self.nombre} {self.comision}"
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=32,blank=True)
    telefono = models.CharField(max_length=20,blank=True)
    email = models.EmailField(blank=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=32,blank=True)
    telefono = models.CharField(max_length=20,blank=True)
    email = models.EmailField()
    biografia = models.TextField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Entrega(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_entrega = models.DateTimeField()
    esta_aprobado = models.BooleanField(default=False)

 