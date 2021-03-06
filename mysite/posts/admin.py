from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
	list_display   = ["__unicode__","title","timestamp"]
	list_editable  = ["title"]	
	list_filter    = ["updated","timestamp"]
	search_fields  = ["title","content"]
	class Meta:
		model = Post



admin.site.register(Post, PostAdmin)
