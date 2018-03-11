from django.conf.urls import patterns, include, url
from apps.portal.views import index

urlpatterns = [
	url(r'^$', index),
	url(r'^asignatura_detalle/', 'apps.portal.views.asignatura_detalle', name='asignatura_detalle'),
	url(r'^carrera_detalle/', 'apps.portal.views.carrera_detalle', name='carrera_detalle'),
	url(r'^recursos_detalle/', 'apps.portal.views.recurso_detalle', name='recurso_detalle'),
	url(r'^usuarios_detalle/', 'apps.portal.views.usuarios_detalle', name='usuario_detalle'),
	url(r'^contactos/', 'apps.portal.views.contactos', name='contactos'),
		
]