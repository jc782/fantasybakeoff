from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User



# Fantasy Bakeoff key models
class Team(models.Model):
	user      = models.OneToOneField(User, on_delete=models.CASCADE)	
	email     = models.EmailField(max_length=150, primary_key=True)	
	team      = models.CharField(max_length=100, verbose_name='Team Name')
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	created   = models.BooleanField(default=True)	

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
	ninth  = models.CharField(max_length=20,choices=CONTESTANT_CHOICES,)
	tenth  = models.CharField(max_length=20,choices=CONTESTANT_CHOICES,)


	def __unicode__(self):
		return self.team

	def get_score(self):
		#spearmans rank on the contestant results.
		CONTESTANT_RESULT = ['Selasi','Rav','Michael','Kate','Lee','Jane','Benjamina','Louise','Candice','Andrew','Val','Tom']
		x1 = CONTESTANT_RESULT.index(self.winner)
		x2 = CONTESTANT_RESULT.index(self.second)-1
		x3 = CONTESTANT_RESULT.index(self.third)-2 
		x4 = CONTESTANT_RESULT.index(self.fourth)-3 
		x5 = CONTESTANT_RESULT.index(self.fifth)-4
		x6 = CONTESTANT_RESULT.index(self.sixth)-5
		x7 = CONTESTANT_RESULT.index(self.seventh)-6 
		x8 = CONTESTANT_RESULT.index(self.eighth)-7
		x9 = CONTESTANT_RESULT.index(self.ninth)-8
		x10= CONTESTANT_RESULT.index(self.tenth)-9
				
		#score = int(100-6*(x1**2+x2**2+x3**2+x4**2+x5**2+x6**2+x7**2+x8**2+x9**2+x10**2)/19.8)	
		score = 'Competition yet to begin'		
		return score

	def get_absolute_url(self):
		return reverse("fbo:home")



class League(models.Model):
	league      = models.CharField(max_length=150, verbose_name='League Name')
	teams       = models.ManyToManyField(Team)
	timestamp   = models.DateTimeField(auto_now=False, auto_now_add=True)
	
	def __unicode__(self):
		return self.league

	def get_absolute_url(self):
		return "/fbo/league/%s/" %self.id
