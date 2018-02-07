from django.contrib import admin

# Register your models here.
from .models import Asignatura
from .models import Carrera
from .models import Recurso

admin.site.register(Asignatura)
admin.site.register(Carrera)
admin.site.register(Recurso)
