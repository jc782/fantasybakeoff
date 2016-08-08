from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
 url(r'^create/$', views.team_create, 'createTeam'), #create the team
 url(r'^index/$', views.team_detail, name='home'), #main home function
 url(r'^edit/$', views.team_update, name='update'), #make team changes
 url(r'^league/(?P<id>\d+)/$', views.league_view, name='league'),
 url(r'^league-create/$', views.league_create, name='createLeague'), #create the team
 ]
