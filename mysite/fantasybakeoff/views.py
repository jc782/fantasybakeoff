from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Team, League
from .forms import TeamForm, LeagueForm, LeagueAdd
# Create your views here.

def team_create(request):
	form = TeamForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		instance.created = True
		messages.success(request,'Successfully Created')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {'form':form}
	return render(request,'team_form.html',context)


def team_detail(request):
	if request.user.is_authenticated():	# check the user is logged in			
		try:		
			t = Team.objects.get(user=request.user) # access their team profile
		except:
			t= 0
		if t:		
			league = t.league_set.all()		
			context = {'Team':t , 'Score':t.get_score(),'Leagues':league}
			return render(request,'team_detail.html',context) # render the details of their team profile
		else:
			return render(request,'howto.html') #no context, effectively a static page


# allow the user to update their team if necessary
def team_update(request):
	team = Team.objects.get(user=request.user)	
	form = TeamForm(request.POST or None, instance=team)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.created = True
		instance.save()
		messages.success(request,'Successfully Created')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {'form':form,
		   'team':team}	
	return render(request,'team_form.html',context)


def league_view(request, id=None):
	league = get_object_or_404(League, id=id)
	return render(request, 'league_detail.html', {'league':league}) 

def league_create(request):
	if request.user.is_authenticated():	
		form = LeagueForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			instance.teams.add(Team.objects.get(user=request.user)) #add initial user 
			instance.save()
			messages.success(request,'Successfully Created')
			return HttpResponseRedirect(instance.get_absolute_url())
		context = {'form':form,}	
		return render(request,'league_form.html',context)	
	else:
		return HttpResponse('Must be logged in to create league')

def league_add(request):
	if request.user.is_authenticated():	
		form = LeagueAdd(request.POST or None)
		if form.is_valid():
			idx = request.POST.get('leaguenumber')
			if League.objects.filter(id=idx).exists():
				obj = League.objects.get(id=idx)
				context = {'league':obj}
				team = Team.objects.get(user=request.user) #find the users team			 
				obj.teams.add(team) # add the users team
				return render(request, 'league_detail.html', context)
			else:
				err_ms  = 'League does not exist, search another league.' 
				context = {'form':form,'league': err_ms}
				return render(request, 'league_add.html', context) 
			league = League.objects.get(id=idx) # find the league from the request
			league.teams.add(team) # add the users team
			return render(request, 'league_detail.html', {'league':league}) 
	return render(request, 'league_add.html', {'form':form})


def homeview(request):
	return render(request, 'home.html')

