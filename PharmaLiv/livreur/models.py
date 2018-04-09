from django.db import models
from PharmaLiv import settings
from django import forms
from patient.models import Patient

class Region(models.Model):
	zoneDeLivraison = models.CharField(max_length=100, null=False)
	region = models.CharField(max_length=100, null=False)

	def __str__(self):
		return self.zoneDeLivraison


class Livreur(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	sexe = models.CharField(max_length=1, null = False)
	dateNaissance = models.DateField(null=False, blank=True)
	telephone = models.IntegerField  (max_length=9)
	adresse = models.CharField(max_length=100, null=False)
	zoneDeLivraison = models.ForeignKey(Region, on_delete=models.CASCADE)


	def __str__(self):
		return self.adresse


class NotificationsLivreur(models.Model):
	livreur = models.ForeignKey(Livreur, on_delete=models.CASCADE)
	pharmacie = models.CharField(max_length=50, null=False)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	nomPatient = models.CharField(max_length = 30, null = False)
	prenomPatient = models.CharField(max_length = 30, null = False)
	adresse = models.CharField(max_length = 100, null = False)
	telephonePatient = models.IntegerField(max_length = 9, null = False)
	commande = models.CharField(max_length = 200, null = False)
	dateCommande = models.DateTimeField(auto_now_add = True, auto_now = False, verbose_name = "Date de la commande")
	dateLivraison = models.DateTimeField(auto_now_add = True, auto_now = False, verbose_name = "Date de livrason")
	lu = models.BooleanField(default=False)
	livree = models.BooleanField(default=False)

