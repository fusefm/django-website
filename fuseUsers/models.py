from django.db import models
from userfn import *
class mailingList(models.Model):
	title = models.CharField(max_length=80)
	dn = models.CharField(max_length=250)
	def __unicode__(self):
		return self.title

class fuseUser(models.Model):
	idnumber = models.CharField('ID Number', max_length = 7)
	mailingList = models.ManyToManyField(mailingList, blank = True)
	firstName = models.CharField('first name', max_length = 25)
	lastname = models.CharField('last name', max_length = 25)
	email = models.EmailField()
	title = models.CharField('Committee Title', max_length = 25, blank = True)
	bio = models.TextField('biography', blank = True)
	mobile = models.CharField(max_length = 11, blank = True)
	picture = models.FileField(upload_to='userpics', blank = True)
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
	homepage = models.URLField(blank = True)
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
