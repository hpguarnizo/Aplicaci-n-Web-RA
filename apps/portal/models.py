from django.db import models

# Create your models here.
class Usuario(models.Model):
	id_usuario=models.AutoField(primary_key=True)
	nombres= models.CharField(max_length=70)
	apellidos= models.CharField(max_length=70)
	correo= models.EmailField(max_length=70)
	telefono= models.CharField(max_length=70)
	nombre_usuario= models.CharField(max_length=100)
	contraseña= models.CharField(max_length=70)
	rol_usuario= models.ForeignKey('RolUsuario', db_column='id_rol')
	fecha_creacion=models.DateField()
	fecha_modificacion= models.DateField()
	def __str__(self):
		return self.nombre_usuario

class RolUsuario(models.Model):
	id_rol= models.AutoField(primary_key=True)
	nombre= models.CharField(max_length=70)
	descripcion = models.TextField()
	def __str__(self):
		return self.nombre



class TipoRecurso(models.Model):
	id_tipo_recurso=models.AutoField(primary_key=True)
	nombre= models.CharField(max_length=30)
	extension= models.CharField(max_length=30)
	descripcion= models.TextField()

	def __str__(self):
		return self.nombre


class Recurso(models.Model):
	id_recurso= models.AutoField(primary_key=True)
	nombre= models.CharField(max_length=255)
	descripcion= models.TextField()
	tipo_recurso= models.ForeignKey('TipoRecurso', db_column='id_tipo_recurso')
	id_usuario= models.ForeignKey('Usuario', db_column='id_usuario')
	archivo_recurso = models.FileField(upload_to='recursos/')
	tag_recurso= models.ForeignKey('TagRecurso',db_column='id_tag')
	qrcode = models.ImageField(upload_to='recursos/', blank=True, null=True)
	def __str__(self):
		return self.nombre

class TagRecurso(models.Model):
	id_tag= models.AutoField(primary_key=True)
	descripcion= models.CharField(max_length=70)

	def __str__(self):
		return self.descripcion

# class Asignatura(models.Model):
# 	id_asignatura= models.AutoField(primary_key=True)
# 	nombre= models.CharField(max_length=255)
# 	descripcion= models.TextField()
# 	fecha_creacion=models.DateField()
# 	fecha_modificacion= models.DateField()
# 	id_carrera=models.ForeignKey('Carrera', db_column='id_carrera' , default="")

# 	def __str__(self):
# 		return self.nombre

# class Carrera(models.Model):
# 	id_carrera=models.AutoField(primary_key=True)
# 	nombre=models.CharField(max_length=255)
# 	descripcion=models.TextField()
# 	fecha_creacion=models.DateField()
# 	fecha_modificacion= models.DateField()
# 	def __str__(self):
# 		return self.nombre