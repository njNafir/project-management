from django.shortcuts import render, HttpResponse, redirect
from django.http import FileResponse
from django.utils.http import is_safe_url
from django.views.generic import View, CreateView
from info.models import Info
from .models import Project 
from .forms import SubmitProjectForm
from django.conf import settings

from mimetypes import guess_type
from wsgiref.util import FileWrapper
import os

def project_page(request):
	info_ = Info.objects.first()
	projects = Project.objects.all()
	context = {
		'info': info_,
		'prs': projects
	}
	return render(request, 'pages/project.html', context)


def single_project(request, group_number, pk, *args, **kwargs):
	info_ = Info.objects.first()
	project = Project.objects.get_by_group_pk(group_number, pk)
	single_project = True
	context = {
		'info': info_,
		'pr': project,
		'single':single_project
	}
	return render(request, 'pages/project.html', context)

def add_project(request):
	add_project = True
	info_ = Info.objects.first()
	# form_ = NormalContactForm
	submit_form_ = SubmitProjectForm
	context = {
		'info':info_,
		'submit_form':submit_form_,
		'add_project':add_project
	}
	hcf_post = SubmitProjectForm(request.POST, request.FILES or None)
	next_page = request.GET.get('next')
	next_post = request.POST.get('next')
	redirect_url = next_page or next_post or None

	if hcf_post.is_valid():		
		instance = hcf_post.save(commit=False)
		instance.save()
		if is_safe_url(redirect_url, request.get_host()):
			return redirect(redirect_url)
	return render(request, 'pages/project.html', context)

# def search_project(request, *args, **kwargs):
# 	query = request.GET.get('search')
# 	print(query)
# 	projects = Project.objects.search(query)
# 	info_ = Info.objects.first()
# 	context = {
# 		'info': info_,
# 		'prs': projects,
# 		'query': query
# 	}
# 	return render(request, 'pages/project.html', context)