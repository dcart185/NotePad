from models import NoteTaker

from rest_framework import serializers

class NoteTakerSerializer(serializers.ModelSerializer):
	class Meta:
		model = NoteTaker
		fields = ('email', 'password','is_staff')
		write_only_fields = ('password',)

	def create(self,validated_data):
		return NoteTaker.objects.create(**validated_data)