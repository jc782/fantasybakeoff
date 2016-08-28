from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
 url(r'^league/(?P<id>\d+)/$', views.league_view, name='detail'),
 url(r'^create/$', views.team_create, name='create'), #create the team
 url(r'^index/$', views.team_detail, name='home'), #main home function
 url(r'^edit/$', views.team_update, name='update'), #make team changes
 url(r'^league-create/$', views.league_create, name='createLeague'), #create the team
 url(r'^league-add/$', views.league_add, name='leagueadd'), 
 url(r'^', views.homeview, name='base'), #main home function
]
