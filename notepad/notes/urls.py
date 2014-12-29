from django.conf.urls import patterns, url, include
#from rest_framework import routers
from notes import views


urlpatterns = patterns('',
	url(r'^hello$',views.hello),
)
