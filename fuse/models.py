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

class mailingList(models.Model):
	title = models.CharField(max_length=80)
	dn = models.CharField(max_length=250)
	def __unicode__(self):
		return self.title

class fuseUser(User):
	mailingList = models.ManyToManyField(mailingList)
	firstName = models.CharField(max_length = 25)
	lastname = models.CharField(max_length = 25)
	bio = models.TextField()
	mobile = models.CharField(max_length = 11)
	def __unicode__(self):
		return firstName + " " + lastname
	def getname(self):
		return firstName + " " + lastname
		

class Program(models.Model):
	name = models.CharField(max_length = 150)
	genre = models.CharField(max_length = 50)
	presenters = models.ManyToManyField(fuseUser)
	description = models.TextField()
	blurb = models.TextField()
	idea = models.TextField()
	homepage = models.URLField()
	dj = models.CharField(max_length = 120)
	shouldBeOnAir = models.TextField()
	shouldntBeOnAir = models.TextField()
	datetime = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.name
	

class Schedule(models.Model):
	program = models.ForeignKey(Program, related_name='schedules')
	DOW  = (
		(0, 'Monday'),
		(1, 'Tuesday'),
		(2, 'Wednesday'),
		(3, 'Thursday'),
		(4, 'Friday'),
		(5, 'Saturday'),
		(6, 'Sunday'))
	dow = models.IntegerField(choices=DOW)
	length = models.IntegerField(default=120)
	time = models.TimeField()
