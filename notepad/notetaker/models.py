from django.db import models

# Create your models here.
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)

class NoteTakerManager(BaseUserManager):

	def create_user(self,email, password):
		if not email:
			raise ValueError('User must have an email address')

		if not password:
			raise ValueError('User must have a password')

		user = self.model(
			email=self.normalize_email(email)
		)

		user.set_password(password)
		user.save()

class NoteTaker(AbstractBaseUser):
	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True
	)

	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = NoteTakerManager()

	class Meta:
		verbose_name="Note Taker"

	USERNAME_FIELD = 'email'

	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.email

	@property 
	def is_staff(self):
		return self.is_admin

	def has_module_perms(self, app_label):
		return self.is_admin
	
	def has_perm(self, perm, obj=None):
		return self.is_admin
