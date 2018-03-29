from django.db import models
from django.utils.text import slugify

# Create your models here.

class Medecin(models.Model):
    profil = models.ImageField(default = 'medecin.jpg', blank = True)
    login = models.CharField(max_length=30, null=False)  
    password = models.CharField(max_length=30,null=False)
    nom = models.CharField(max_length=30, null = False)
    prenom = models.CharField(max_length=30, null = False)
    dateNaissance = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de naissance")
    telephone = models.IntegerField(max_length = 9, null = False)
    specialite = models.CharField(max_length=30, null = False)
    hopital = models.CharField(max_length=30, null = False)
    slug = models.SlugField()
    
    def __str__(self):
        return self.profil, self.nom, self.prenom, self.specialite, self.hopital

    def _get_unique_slug(self):
        slug = slugify(self.nom)
        unique_slug = slug
        num = 1
        while Medecin.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()
    


