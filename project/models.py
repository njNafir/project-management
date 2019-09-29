from django.db import models
from django.urls import reverse

def image_upload_path(instance, filename):
	group_number = instance.group_number
	path 	= "project_thumbnail/{group_number}/{filename}".format(group_number=group_number, filename=filename)
	return path

def project_proposal_upload_path(instance, filename):
	group_number = instance.group_number
	path 	= "project_proposal/{group_number}/{filename}".format(group_number=group_number, filename=filename)
	return path

def file_upload_path(instance, filename):
	group_number = instance.group_number
	path 	= "project_file/{group_number}/{filename}".format(group_number=group_number, filename=filename)
	return path

class ProjectQuerySet(models.query.QuerySet):
	def approved(self):
		return self.filter(approved=True)

	def search(self, query):
		lookups = Q(subtitle__icontains=query)|Q(group_name__icontains=query)|Q(members_name__icontains=query)|Q(used_skill__icontains=query)|Q(title__icontains=query)|Q(description__icontains=query)
		return self.filter(lookups).distinct()

class ProjectManager(models.Manager):
	def get_queryset(self):
		return ProjectQuerySet(self.model, using=self._db)

	def all(self):
		return self.get_queryset().approved()

	def get_by_group_pk(self, group_number, pk):
		qs = self.get_queryset().filter(group_number=group_number, pk=pk, approved=True)
		if qs.count()==1:
			return qs.first()
		else:
			return None

	def search(self, query):
		return self.get_queryset().approved().search(query)

class Project(models.Model):
	group_number 		= models.PositiveIntegerField()
	group_name 			= models.CharField(max_length=120)
	members_name 		= models.CharField(max_length=254)
	title 				= models.CharField(max_length=254)
	subtitle 			= models.CharField(max_length=254, blank=True, null=True)
	description 		= models.TextField()
	used_skill			= models.CharField(max_length=254)
	thumbnail			= models.ImageField(upload_to=image_upload_path)
	project_proposal	= models.FileField(upload_to=project_proposal_upload_path)
	project_file		= models.FileField(upload_to=file_upload_path)
	approved 			= models.BooleanField(default=False)
	timestamp 			= models.DateTimeField(auto_now_add=True)
	updated 			= models.DateTimeField(auto_now=True)

	objects 		= ProjectManager()

	class Meta:
		ordering = [
			'group_number',
			'-updated',
			'-timestamp'
		]

	def __str__(self):
		return self.group_name

	def get_name(self):
		return self.title

	def get_absolute_url(self):
		return reverse("single_project", kwargs={"group_number":self.group_number, "pk":self.pk})