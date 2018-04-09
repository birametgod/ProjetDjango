from django.db import models
from PharmaLiv import settings
from django import forms

# Create your models here.

class userAdmin(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

	def __str__(self):
		return self.adresse
