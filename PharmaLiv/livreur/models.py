from django.db import models
from PharmaLiv import settings
from django import forms
from patient.models import Patient
from pharmacie.models import Commandes_Effectuees

class Region(models.Model):
	choices={
		('dakar', 'Dakar'),
		('thies', 'Thiès'),
		('Saint-Louis', 'Saint-Louis'),
		('Mbour', 'Mbour'),
		('Fatick', 'Fatick'),
		('Kaolack', 'Kaolack'),
		('Louga', 'Louga')
	}
	zoneDeLivraison = models.CharField(max_length=100, null=False)
	region = models.CharField(max_length=10, choices=choices)

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
	commande =models.ForeignKey(Commandes_Effectuees, on_delete=models.CASCADE)
	dateCommande = models.DateTimeField(auto_now_add = True, auto_now = False, verbose_name = "Date de la commande")
	dateLivraison = models.DateTimeField(auto_now_add = True, auto_now = False, verbose_name = "Date de livrason")
	lu = models.BooleanField(default=False)
	livree = models.BooleanField(default=False)

	def __str__(self):
    		return self.adresse
