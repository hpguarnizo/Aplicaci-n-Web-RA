from django.shortcuts import render
from django.http import HttpResponse
from apps.portal.models import *
from .models import Asignatura
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