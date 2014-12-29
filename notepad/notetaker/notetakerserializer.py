from models import NoteTaker

from rest_framework import serializers

class NoteTakerSerializer(serializers.ModelSerializer):
	class Meta:
		model = NoteTaker
		fields = ('email', 'is_staff')
