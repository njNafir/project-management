from django.contrib import admin
from .models import Info

class AdminInfo(admin.ModelAdmin):
	list_display 		= ['title', 'name', 'position']
	list_filter			= ['updated', 'timestamp']
	search_field		= ['position', 'quote', 'objective', 'description']
	ordering 			= ['-updated', '-timestamp']

admin.site.register(Info, AdminInfo)