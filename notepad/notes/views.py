from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from notes.models import Note
from notes.noteserializer import NoteSerializer


# Create your views here.

def index(request):
	return render(request,'index.html',{})

def hello(request):
	return HttpResponse("hello jack!")


class NotesView(APIView):


	#returns a list of notes for the user
	def get(self,request):
		user = self.request.user
		notes = Note.objects.filter(noteowner=user)
		serializer = NoteSerializer(notes, many=True)
		return Response(serializer.data)
