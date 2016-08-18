from django import forms
from .models import Team, League

class TeamForm(forms.ModelForm):
	class Meta:
		model = Team
		fields = ["team","winner","second","third","fourth","fifth","sixth","seventh","eighth","nineth","tenth"]

	def clean(self):
		form_data = self.cleaned_data #check if the entered set has any repeat values
		a = [form_data['winner']]
		a.append(form_data['second'])
		a.append(form_data['third'])
		a.append(form_data['fourth'])
		a.append(form_data['fifth'])
		a.append(form_data['sixth'])
		a.append(form_data['seventh'])
		a.append(form_data['eighth'])
		a.append(form_data['nineth'])
		a.append(form_data['tenth'])
		
		temp = set(a)
		result = {}
		for i in temp:
			result[i]=a.count(i)
		if any(v>1 for v in result.itervalues()):
			self._errors["winner"]=["Repeated constestants - please enter a valid set"]		
		return form_data

class LeagueForm(forms.ModelForm):
	class Meta:
		model = League
		fields = ["league"]

class LeagueAdd(forms.Form):
	leaguenumber = forms.CharField(label='League Number', max_length=8)
	class Meta:
		fields=["leaguenumber"]

