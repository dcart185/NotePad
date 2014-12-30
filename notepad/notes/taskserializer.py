from notes.models import Task,Note

from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):

	note = serializers.PrimaryKeyRelatedField(queryset=Note.objects.all())

	class Meta:
		model = Task
		fields = ('id','task','created_date','updated_date','note')