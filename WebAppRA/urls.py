from django.conf.urls import patterns, include, url

from django.contrib import admin
from apps.portal.views import *
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WebAppRA.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('apps.portal.urls')),
    url(r'^asignatura_detalle/', 'apps.portal.views.asignatura_detalle', name='asignatura_detalle'),
    url(r'^carrera_detalle/', 'apps.portal.views.carrera_detalle', name='carrera_detalle'),
    url(r'^usuarios_detalle/', 'apps.portal.views.usuarios_detalle', name='usuarios_detalle'),
    url(r'^recursos_detalle/', 'apps.portal.views.recurso_detalle', name='recurso_detalle'),
#    url(r'^logueado', include('apps.portal.urls')),
)
