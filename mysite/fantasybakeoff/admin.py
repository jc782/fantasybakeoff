from django.contrib import admin
from .models import Team, League

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
	list_display = ["user","team","timestamp"]
	class Meta:
		model=Team

class LeagueAdmin(admin.ModelAdmin):
	list_display = ["id","league","timestamp"]
	class Meta:
		model=League


admin.site.register(Team, TeamAdmin)
admin.site.register(League, LeagueAdmin)
