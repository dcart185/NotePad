
from rest_framework import permissions

SAFE_METHODS = ['POST',]

class NoteTakerPermission(permissions.BasePermission):
	"""
	Global permission for NoteTakerView
	"""

	def has_permission(self, request,view):
		if(request.method == "POST" or
			request.user and request.user.is_authenticated()):
			return True
		return False