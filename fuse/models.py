from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
	name = models.CharField(max_length = 50)
	def __unicode__(self):
		return name

class Story(models.Model):
	department = models.ForeignKey(Department)
	title = models.CharField(max_length = 150)
	body = models.TextField()
	def __unicode__(self):
		return title

