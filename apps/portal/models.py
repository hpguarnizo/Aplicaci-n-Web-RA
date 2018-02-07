from django.db import models

# Create your models here.
TIPO_RECURSOS_CHOICES=(
	('Imagen','Imagen'),
	('Video','Video'),
	('3D','3D'),
	('PDF','PDF'),
	('MP3','MP3')
)

class Recurso(models.Model):
	id_recurso= models.AutoField(primary_key=True, default="")
	nombre= models.CharField(max_length=255)
	descripcion= models.TextField()
	tipo_recurso= models.CharField(max_length=50, choices= TIPO_RECURSOS_CHOICES, default="")
	id_asignatura= models.ForeignKey('Asignatura', db_column='id_asignatura', default="")
	archivo_recurso = models.FileField(upload_to='static/')
	def __str__(self):
		return self.nombre

class Asignatura(models.Model):
	id_asignatura= models.AutoField(primary_key=True)
	nombre= models.CharField(max_length=255)
	descripcion= models.TextField()
	fecha_creacion=models.DateField()
	fecha_modificacion= models.DateField()
	id_carrera=models.ForeignKey('Carrera', db_column='id_carrera' , default="")

	def __str__(self):
		return self.nombre

class Carrera(models.Model):
	id_carrera=models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=255)
	descripcion=models.TextField()
	fecha_creacion=models.DateField()
	fecha_modificacion= models.DateField()
	def __str__(self):
		return self.nombre