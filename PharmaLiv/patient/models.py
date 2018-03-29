from django.db import models

# Create your models here.
class Patient(models.Model):
    login = models.CharField(max_length=30,null=False,unique=True)  #Le paramètre null, lorsque mis à True, indique à Django que ce champ peut être laissé vide et qu'il est donc optionnel.  
    password = models.CharField(max_length=30,null=False)
    nom = models.CharField(max_length=30, null = False)
    prenom = models.CharField(max_length=30, null = False)
    sexe = models.CharField(max_length=30, null = False)
    allergie = models.CharField(max_length=100, null = False)
    traitement = models.CharField(max_length=100,null=False)
    dateNaissance = models.DateTimeField(auto_now_add=True, auto_now=False,
    verbose_name="Date de naissance")
    
    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.nom 

    def __unicode__(self):
        return 
