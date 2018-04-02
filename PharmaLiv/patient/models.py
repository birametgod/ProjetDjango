from django.db import models
from PharmaLiv import settings
from medecin.models import Medecin
from django import forms
# Create your models here.
class Patient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    sexe = models.CharField(max_length=100, null = False)
    allergie = models.CharField(max_length=100, null = False)
    traitement = models.CharField(max_length=100,null= False)
    dateNaissance = models.DateField(null=True, blank=True)
    adresse = models.CharField(max_length=100, null=False)

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.nom 

    def __unicode__(self):
        return 

class Ordonnances(models.Model):
    libelle = models.CharField(max_length=255, null=False)
    medicaments = models.ImageField(default='default.png', blank=True)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE) # en cas de suppression de la catégorie, tous les articles ayant cette catégorie seront également supprimé (provoquant une cascade de suppression) ;
    medecin = models.ForeignKey(Medecin,on_delete=models.CASCADE)
    def __str__(self):
        return self.libelle

    def __unicode__(self):
        return 

