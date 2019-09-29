from django.db import models

class Info(models.Model):
	title 			= models.CharField(max_length=120)
	name 			= models.CharField(max_length=30)
	position 		= models.CharField(max_length=254, blank=True, null=True)
	quote 			= models.CharField(max_length=254, blank=True, null=True)
	objective 		= models.TextField()
	description 	= models.TextField()
	process 		= models.TextField(blank=True, null=True)
	experience		= models.TextField(blank=True, null=True)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title