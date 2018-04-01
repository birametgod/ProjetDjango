from django.db import models
from PharmaLiv import settings

# Create your models here.

class Medecin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    dateNaissance = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de naissance")
    telephone = models.IntegerField(max_length = 9, null = False)
    specialite = models.CharField(max_length=30, null = False)
    hopital = models.CharField(max_length=30, null = False)
    

    def __str__(self):
        return self.nom


    def __unicode__(self):
        return 