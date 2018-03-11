from django.shortcuts import render
from django.http import HttpResponse
from apps.portal.models import *
from django.db import models
from django.contrib.auth.models import User

# Create your views here.

def index(request):
	return render(request,'index.html')

def logueado(request):
	return render(request,'logueado.html')

def asignatura_detalle(request):
	asignaturas = Asignatura.objects.all()
	return render(request,'asignatura_detalle.html', {'asignaturas':asignaturas})

def carrera_detalle(request):
	carreras = Carrera.objects.all()
	return render(request,'carrera_detalle.html', {'carreras':carreras})

def usuarios_detalle(request):
	usuarios = User.objects.all()
	return render(request,'usuarios_detalle.html', {'usuarios':usuarios})

def recurso_detalle(request):
	recursos = Recurso.objects.all()
	return render(request,'recursos_detalle.html', {'recursos':recursos})

def contactos(request):
	return render(request,'contactos.html')

def quienes_somos(request):
	return render(request,'quienes_somos.html')

def generarQR (request):

	id_recurso = request.GET.get('id')
	recurso = Recurso.objects.filter(id_recurso=id_recurso)
	print (id_recurso)
	qr = qrcode.QRCode(
		error_correction=qrcode.constants.ERROR_CORRECT_H,
		version=1,
		box_size=10,
		border=4,
	)
	qr.add_data('http://www.ks7000.net.ve')
	qr.make(fit=True) 
	imagen = qr.make_image()
	imagen.save('ks7000_url_qr.png', 'png')

	img = qr.make_image()
	return render(request, 'empresas_detalle.html', {'empresa':empresa, 'all_empresa':all_empresa})
