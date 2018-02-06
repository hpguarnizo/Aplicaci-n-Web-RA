from django.db import models

# Create your models here.

class Recurso(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=150)


class Asignatura(models.Model):
	id_asignatura= models.AutoField(primary_key=True)
	nombre= models.CharField(max_length=255)
	descripcion= models.TextField()
	fecha_creacion=models.DateField()
	fecha_modificacion= models.DateField()



	def __str__(self):
		return self.nombre

class Carrera(models.Model):
	id_carrera=models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=255)
	descripcion=models.TextField()
	fecha_creacion=models.DateField()
	fecha_modificacion= models.DateField()
	