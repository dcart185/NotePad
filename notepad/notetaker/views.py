from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from notetakerserializer import NoteTakerSerializer
from models import NoteTaker

@api_view(['GET'])
def notetaker_detail(request):

	try:
		email = request.GET.get("email",None)

		if email is None:
			return Response({"error":"Must include note taker's email"})
		
		elif email == request.user.email:
			notetaker = NoteTaker.objects.get(email=email)
		
		else:
			return Response({"error":"You do not have permission"})
	
	except NoteTaker.DoesNotExist:
		return Response({"error":"Note taker does not exist"})

	if request.method == 'GET':
		serializer = NoteTakerSerializer(notetaker)
		return Response(serializer.data)

