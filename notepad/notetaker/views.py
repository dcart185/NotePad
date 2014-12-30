from django.shortcuts import render

# Create your views here.
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from notetakerserializer import NoteTakerSerializer
from notetakerpermission import NoteTakerPermission
from models import NoteTaker


class NoteTakerView(APIView):

	permission_classes = (NoteTakerPermission,)

	def get(self,request):
		try:
			notetaker = NoteTaker.objects.get(email=request.user.email)
			serializer = NoteTakerSerializer(notetaker)
			return Response(serializer.data)
		except NoteTaker.DoesNotExist:
			return Response({"error":"Note taker does not exist"},
				status=status.HTTP_400_BAD_REQUEST)

	
	def post(self,request):
		serializer = NoteTakerSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




