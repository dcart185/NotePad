from django.contrib import admin

# Register your models here.
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from models import NoteTaker

class NoteTakerCreationForm(forms.ModelForm):
	password1 = forms.CharField(label = 'Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label = 'Password confirmation', widget=forms.PasswordInput)

	class Meta:
		model = NoteTaker
		fields = ('email', 'is_admin')

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")

		return password2

	def save(self, commit = True):
		user = super(NoteTakerCreationForm,self).save(commit=False)
		print self.cleaned_data["password1"]
		user.set_password(self.cleaned_data["password1"])

		if commit:
			user.save()
		return user


class NoteTakerChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = NoteTaker
		fields = ('email','password','is_active','is_admin')

	def clean_password(self):
		return self.initial["password"]

class NoteTakerAdmin(UserAdmin):
	form = NoteTakerChangeForm
	add_form = NoteTakerCreationForm

	list_display = ('email','is_staff','is_admin')
	list_filter = ('is_admin',)
	
	fieldsets = (
		(None, {'fields':('email','password')}),
		('Permissions',{'fields':('is_admin',)}),
	)

	
	add_fieldsets = (
		(None,{
			'classes':('wide',),
			'fields':('email','password1','password2')}
		),
	)

	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ()

admin.site.register(NoteTaker,NoteTakerAdmin)

admin.site.unregister(Group)


