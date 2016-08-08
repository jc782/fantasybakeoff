from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import uuid



# Fantasy Bakeoff key models
class Team(models.Model):
	user      = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	team      = models.CharField(max_length=100)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	score     = models.IntegerField(default=0)
	
	CONTESTANT_CHOICES = (
		('JO', 'Josh'),
		('NA', 'Nadiya'),
		('EM', 'Emma'),	
	)

	winner = models.CharField(max_length=2,choices=CONTESTANT_CHOICES,)
	second = models.CharField(max_length=2,choices=CONTESTANT_CHOICES,)
	third = models.CharField(max_length=2,choices=CONTESTANT_CHOICES,)


	def __unicode__(self):
		return self.team

	def get_score(self):
		return self.score

	def get_absolute_url(self):
		return reverse("fbo:home")



class League(models.Model):
	league      = models.CharField(max_length=100)
	teams       = models.ManyToManyField(Team)
	timestamp   = models.DateTimeField(auto_now=False, auto_now_add=True)
	
	def __unicode__(self):
		return self.league
	
	def get_absolute_url(self):
		return reverse("fbo:league", kwargs={'id': self.id})


