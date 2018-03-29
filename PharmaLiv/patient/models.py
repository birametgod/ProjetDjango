from django.db import models

# Create your models here.
class Patient(models.Model):
    login = models.CharField(max_length=30,null=True)  #Le paramètre null, lorsque mis à True, indique à Django que ce champ peut être laissé vide et qu'il est donc optionnel.  
    password = models.CharField(max_length=30,null=True)
    nom = models.CharField(max_length=30, null = True)
    prenom = models.CharField(max_length=30, null = True)
    sexe = models.CharField(max_length=30, null = True)
    allergie = models.CharField(max_length=100, null = True)
    traitement = models.CharField(max_length=100,null=True)
    dateNaissance = models.DateTimeField(auto_now_add=True, auto_now=False,
    verbose_name="Date de naissance")
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
