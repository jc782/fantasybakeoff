from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Team, League
from .forms import TeamForm, LeagueForm
# Create your views here.

def team_create(request):
	form = TeamForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,'Successfully Created')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {'form':form,}	
	return render(request,'team_form.html',context)


def team_detail(request):
	if request.user.is_authenticated():	# check the user is logged in	
		t = Team.objects.get(user=request.user) # access their team profile
		context = {'Team':t}
		return render(request,'team_detail.html',context) # render the details of their team profile
	else:
		return HttpResponse('Not Logged in')


# allow the user to update their team if necessary
def team_update(request):
	team = Team.objects.get(user=request.user)	
	form = TeamForm(request.POST or None, instance=team)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,'Successfully Created')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {'form':form,
		   'team':team}	
	return render(request,'team_form.html',context)


def league_view(request, id):
	league = get_object_or_404(League, id=id)
	return render(request, 'league_detail.html', {'league':league}) 

def league_create(request):
	if request.user.is_authenticated():	
		form = LeagueForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request,'Successfully Created')
			return HttpResponseRedirect(instance.get_absolute_url())
		context = {'form':form,}	
		return render(request,'league_form.html',context)	
	else:
		return HttpResponse('Must be logged in to create league')






