from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Content(models.Model):
	title = models.CharField(max_length=50)
	location = models.CharField(max_length = 200)
	description = models.TextField(max_length=500)
	slugger = models.SlugField(max_length=30);

	def __unicode__(self):
		return self.slugger

class Contact(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	message = models.TextField(max_length=500)

	def __unicode__(self):
		return self.name
		super(Contact, self).__init__(*args, **kwargs)