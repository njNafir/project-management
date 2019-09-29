from django.shortcuts import render
from info.models import Info
from project.models import Project

def home_page(request):
	info = Info.objects.first()
	projects = Project.objects.all()[:3]
	home_page = True
	context = {
		'title': 'ProPro | Project proposal manager.',
		'info': info,
		'prs':projects,
		'home_page': home_page
	}
	return render(request, 'pages/home.html', context)

def about_page(request):
	info = Info.objects.first()
	context = {
		'info': info,
	}
	return render(request, 'pages/about.html', context)