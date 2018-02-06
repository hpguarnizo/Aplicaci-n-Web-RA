from django.conf.urls import patterns, include, url
from apps.portal.views import index

urlpatterns = [
	url(r'^$', index),
	
]