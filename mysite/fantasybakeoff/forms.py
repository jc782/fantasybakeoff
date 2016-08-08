from django import forms
from .models import Team, League

class TeamForm(forms.ModelForm):
	class Meta:
		model = Team
		fields = ["team","winner","second","third"]


class LeagueForm(forms.ModelForm):
	class Meta:
		model = League
		fields = ["league"]


