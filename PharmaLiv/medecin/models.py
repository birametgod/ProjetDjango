from django.db import models

# Create your models here.

class Medecin(models.Model):
    login = models.CharField(max_length=30, null=False)  
    #Le paramètre null, lorsque mis à False, indique à Django que ce champ ne peut être laissé vide et qu'il n'est donc pas optionnel.  
    password = models.CharField(max_length=30,null=False)
    nom = models.CharField(max_length=30, null = False)
    prenom = models.CharField(max_length=30, null = False)
    dateNaissance = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de naissance")
    specialite = models.CharField(max_length=30)


    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.nom 


    def __unicode__(self):
        return 


