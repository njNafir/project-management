from django.contrib import admin
from .models import Project

class AdminProject(admin.ModelAdmin):
	list_display 		= ['group_number', 'group_name', 'title', 'subtitle']
	list_filter  		= ['approved', 'timestamp', 'updated']
	search_fields 		= ['group_name', 'members_name', 'title', 'subtitle', 'description']
	ordering 	 		= ['group_number', '-updated', '-timestamp']

admin.site.register(Project, AdminProject)