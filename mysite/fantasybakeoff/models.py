from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User



# Fantasy Bakeoff key models
class Team(models.Model):
	user      = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	team      = models.CharField(max_length=100)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	created   = models.BooleanField(default=False)	

	CONTESTANT_CHOICES = (
		('Andrew', 'Andrew'),
		('Candice', 'Candice'),
		('Louise', 'Louise'),
		('Benjamina', 'Benjamina'),
		('Jane', 'Jane'),
		('Lee', 'Lee'),
		('Kate', 'Kate'),
		('Michael', 'Michael'),
		('Rav', 'Rav'),
		('Selasi', 'Selasi'),
		('Val', 'Val'),
		('Tom', 'Tom'),											
	)

	winner  = models.CharField(max_length=20,choices=CONTESTANT_CHOICES,)
	second  = models.CharField(max_length=20,choices=CONTESTANT_CHOICES,)
	third   = models.CharField(max_length=20,choices=CONTESTANT_CHOICES,)
	fourth  = models.CharField(max_length=20,choices=CONTESTANT_CHOICES,)
	fifth   = models.CharField(max_length=20,choices=CONTESTANT_CHOICES,)
	sixth   = models.CharField(max_length=20,choices=CONTESTANT_CHOICES,)
	seventh = models.CharField(max_length=20,choices=CONTESTANT_CHOICES,)
	eighth  = models.CharField(max_length=20,choices=CONTESTANT_CHOICES,)
	nineth  = models.CharField(max_length=20,choices=CONTESTANT_CHOICES,)
	tenth  = models.CharField(max_length=20,choices=CONTESTANT_CHOICES,)


	def __unicode__(self):
		return self.team

	def get_score(self):
		CONTESTANT_RESULT = ['NA','NA','NA','NA','NA','NA','NA','NA','NA','NA']
		#x1 = CONTESTANT_RESULT.index(self.winner) #zero indexed
		#x2 = CONTESTANT_RESULT.index(self.second)
		#x3 = CONTESTANT_RESULT.index(self.third)
		score = 'Competition yet to begin'#x3+x2+x1
		return score

	def get_absolute_url(self):
		return reverse("fbo:home")



class League(models.Model):
	league      = models.CharField(max_length=100)
	teams       = models.ManyToManyField(Team)
	timestamp   = models.DateTimeField(auto_now=False, auto_now_add=True)
	
	def __unicode__(self):
		return self.league

	def get_absolute_url(self):
		return "/fbo/league/%s/" %self.id
