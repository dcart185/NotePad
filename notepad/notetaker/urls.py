from django.conf.urls import patterns, url, include
#from rest_framework import routers
from notetaker import views

urlpatterns = patterns('',
	url(r'^$',views.notetaker_detail),
)