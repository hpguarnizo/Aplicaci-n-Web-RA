from django.contrib import admin

# Register your models here.
from .models import Asignatura
from .models import Carrera

admin.site.register(Asignatura)
admin.site.register(Carrera)