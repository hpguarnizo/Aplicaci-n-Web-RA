from django.contrib import admin

# Register your models here.
from .models import Usuario
from .models import RolUsuario
from .models import Recurso
from .models import TipoRecurso
from .models import TagRecurso

admin.site.register(RolUsuario)
admin.site.register(Usuario)
admin.site.register(Recurso)
admin.site.register(TipoRecurso)
admin.site.register(TagRecurso)
