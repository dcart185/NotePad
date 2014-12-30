from django.shortcuts import render, HttpResponse
from rest_framework import authentication, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from notes.models import Note,Task
from notes.noteserializer import NoteSerializer
from notes.taskserializer import TaskSerializer
from notetaker.models import NoteTaker
from rest_framework.parsers import JSONParser



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

class NoteView(APIView):
	#returns the specific note
	def get(self,request,note_id=None):
		if note_id is None:
			return Response({"error":"A note id is needed"},
				status=status.HTTP_400_BAD_REQUEST)
		
		try:
			note = Note.objects.get(pk=note_id)
		except Note.DoesNotExist:
			return Response({"error":"Note does not exist."},
				status=status.HTTP_400_BAD_REQUEST)

		#may change when one starts sharing notes with friends
		if note.noteowner.email != request.user.email:
			return Response({"error":"You do not have permission."},
				status=status.HTTP_403_FORBIDDEN)
		
		serializer = NoteSerializer(note)
		return Response(serializer.data)

	#creates a new note
	def post(self,request,note_id=None):
		try:
			noteowner = NoteTaker.objects.get(email=request.user.email)
		except NoteTaker.DoesNotExist:
			return Response({"error":"User does not exist."},
				status=status.HTTP_400_BAD_REQUEST)

		serializer = NoteSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save(noteowner=noteowner)
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	#delete note
	def delete(self,request,note_id=None):
		if note_id is None:
			return Response({"error":"A note id is needed"},
				status=status.HTTP_400_BAD_REQUEST)

		try:
			note = Note.objects.get(pk=note_id)
		except Note.DoesNotExist:
			return Response({"error":"Note does not exist"})

		#may change when one starts sharing notes with friends
		if note.noteowner.email != request.user.email:
			return Response({"error":"You do not have permission."},
				status=status.HTTP_403_FORBIDDEN)

		note.delete()

		return Response({"success":"Note deleted"})


class TaskView(APIView):
	#returns the specific Task
	def get(self,request,task_id=None,note_id=None):
		if task_id is None:
			return Response({"error":"a task id is required"},
				status=status.HTTP_400_BAD_REQUEST)
		try:
			task = Task.objects.get(pk=task_id)
		except Task.DoesNotExist:
			return Response({"error":"Task does not exist."},
				status=status.HTTP_400_BAD_REQUEST)

		user =request.user
		if (task.task_writer != user) or (task.note.noteowner != user):
			return Response({"error":"You do not have permission."},
				status=status.HTTP_403_FORBIDDEN)

		serializer = TaskSerializer(task)
		return Response(serializer.data)

	def post(self,request,task_id=None):
		try:
			task_writer = NoteTaker.objects.get(email=request.user.email)
		except NoteTaker.DoesNotExist:
			return Response({"error":"User does not exist."},
				status=status.HTTP_400_BAD_REQUEST)

		serializer=TaskSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save(task_writer=task_writer)
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

