from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
 url(r'^create/$', views.post_create),
 url(r'^(?P<id>\d+)/$', views.post_detail, name='detail'),
 url(r'^list/$', views.post_list, name='list'),
 url(r'^(?P<id>\d+)/edit/$', views.post_update, name='update'),
 url(r'^(?P<id>\d+)/delete/$', views.post_delete),
]
