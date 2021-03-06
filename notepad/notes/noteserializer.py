from notes.models import Note

from rest_framework import serializers
from notetaker.notetakerserializer import NoteTakerSerializer
from notes.taskserializer import TaskSerializer
from notetaker.models import NoteTaker

class NoteSerializer(serializers.ModelSerializer):

	task_set = TaskSerializer(many=True,read_only=True)
	
	class Meta:
		model = Note
		fields = ('id','title','created_date','updated_date','task_set',)

	def create(self,validated_data):
		return Note.objects.create(**validated_data)