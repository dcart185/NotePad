from django.db import models
from notetaker.models import NoteTaker

class Note(models.Model):
	title = models.CharField(max_length=255)
	created_date = models.DateTimeField('date created',auto_now_add=True)
	updated_date = models.DateTimeField('date updated',auto_now=True)
	noteowner= models.ForeignKey(NoteTaker,blank=False,null=False)

class Task(models.Model):
	task = models.TextField()
	note = models.ForeignKey(Note,blank=False,null=False)
	created_date = models.DateTimeField('date created',auto_now_add=True)
	updated_date = models.DateTimeField('date updated',auto_now=True)
	task_completed = models.BooleanField('task_completed',default=False)
	task_writer= models.ForeignKey(NoteTaker,blank=False,null=False)

	def can_edit(self,user):
		return (self.user == task_writer or self.user.is_staff or 
			self.user == self.note.noteowner)





