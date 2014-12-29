from notes.models import Note

from rest_framework import serializers
from notetaker.notetakerserializer import NoteTakerSerializer
from notes.taskserializer import TaskSerializer

class NoteSerializer(serializers.ModelSerializer):

	task_set = TaskSerializer(many=True,read_only=True)

	class Meta:
		model = Note
		fields = ('title','created_date','updated_date','task_set')