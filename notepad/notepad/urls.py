from django.conf.urls import patterns, include, url
from django.contrib import admin
from notes.views import NotesView

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'notepad.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^login/','rest_framework_jwt.views.obtain_jwt_token'),
	url(r'^notetaker/',include('notetaker.urls')),
	url(r'^notes/',NotesView.as_view()),
	url(r'^.$','notes.views.index')
)
