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
	lastName = models.CharField('last name', max_length = 25)
	email = models.EmailField()
	title = models.CharField('Committee Title', max_length = 25, blank = True)
	bio = models.TextField('biography', blank = True)
	mobile = models.CharField(max_length = 11, blank = True)
	picture = models.FileField(upload_to='userpics', blank = True)
	def __unicode__(self):
		return self.idnumber + ' (' +  self.firstName + " " + self.lastName + ')'
	def getname(self):
		return firstName + " " + lastname
	def save(self):
		saveUserToLDAP(self)
		super(fuseUser, self).save()
	def syncUsers(self):
		super(fuseUser, self).save()

class Program(models.Model):
	name = models.CharField('Show Name', max_length = 150)
	genre = models.CharField('Genre of show', max_length = 50)
	presenters = models.ManyToManyField(fuseUser)
	description = models.TextField('Description Of Your Idea')
	blurb = models.TextField('Show Blurb')
	idea = models.TextField('One Original Idea For Your Show')
	homepage = models.URLField('Show Homepage', blank = True)
	dj = models.CharField('Favourite Radio DJ', max_length = 120)
	shouldBeOnAir = models.TextField('Why You Should Be On Air')
	shouldntBeOnAir = models.TextField(' Why You Shouldnt Be On Air')
	datetime = models.CharField('Prefered Time', max_length = 100)
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
