from django.conf.urls import patterns, include, url
from django.contrib import admin
from notes.views import NotesView, NoteView, TaskView
from notetaker.views import NoteTakerView


urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'notepad.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^login/','rest_framework_jwt.views.obtain_jwt_token'),
	url(r'^notetaker',NoteTakerView.as_view()),
	url(r'^notes/',NotesView.as_view()),
	url(r'^note/$',NoteView.as_view()),
	url(r'^note/(?P<note_id>\d+)/$',NoteView.as_view()),
	url(r'^task/$',TaskView.as_view()),
	url(r'^task/(?P<task_id>\d+)/$',TaskView.as_view()),
	url(r'^$','notes.views.index')
)
