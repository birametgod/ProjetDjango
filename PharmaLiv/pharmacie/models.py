from django.db import models
from django.utils.text import slugify

# Create your models here.


class Pharmacie(models.Model):
    login = models.CharField(max_length = 30, null = False)  
    password = models.CharField(max_length = 30, null = False)
    profil = models.ImageField(default = 'pharmacie.jpg', blank = True)
    nom = models.CharField(max_length = 50, null = False)
    adresse = models.CharField(max_length = 100, null = False)
    telephone = models.IntegerField(max_length = 9, null = False)
    horaire = models.CharField(max_length = 50, null = False)
    slug = models.SlugField()

    def __str__(self):
        return self.nom, self.adresse, self.telephone, self.horaire
    

    def _get_unique_slug(self):
        slug = slugify(self.nom)
        unique_slug = slug
        num = 1
        while Pharmacie.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()


class Fiche_Produit(models.Model):
    titre = models.CharField(max_length = 50, null = False)
    photo = models.ImageField(default = 'default.jpg', blank = True)
    prix = models.IntegerField(max_length=10, null = False)
    description = models.TextField(max_length=200, default='DESC', null = False)
    types = models.CharField(max_length = 10, default = 'Pharmacie', null = False)
    nom = models.ForeignKey(Pharmacie, on_delete = models.CASCADE, null = False)
    slug = models.SlugField()

    def __str__(self):
        return self

    def _get_unique_slug(self):
        slug = slugify(self.titre)
        unique_slug = slug
        num = 1
        while Fiche_Produit.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

    @classmethod
    def produits(cls):
        return cls.objects.filter('titre').order_by('prix')

    @classmethod
    def liste_produits(cls, types):
        return cls.publiees().filter(types=types)

    @classmethod
    def search(klass, query):
        if query == '':
            return []
        else:
            return klass.publiees().filter(titre__contains=query)



class Commandes_Effectuees(models.Model):
    nomPatient = models.CharField(max_length = 30, null = False)
    prenomPatient = models.CharField(max_length = 30, null = False)
    adresse = models.CharField(max_length = 100, null = False)
    telephonePatient = models.IntegerField(max_length = 9, null = False)
    commande = models.CharField(max_length = 200, null = False)
    dateCommande = models.DateTimeField(auto_now_add = True, auto_now = False, verbose_name = "Date de la commande")
    dateLivraison = models.DateTimeField(auto_now_add = True, auto_now = False, verbose_name = "Date de livrason")
    livree = models.BooleanField(default = False)
    slug = models.SlugField()

    def __str__(self):
    	return self

    def _get_unique_slug(self):
        slug = slugify(self.nomPatient)
        unique_slug = slug
        num = 1
        while Commandes_Effectuees.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

    @classmethod
    def commandes(cls):
        return cls.objects.filter('nomPatient').order_by('dateCommande', 'dateLivraison')

    @classmethod
    def liste_commandes(cls):
        return cls.commandes().filter(livree=False)

    @classmethod
    def search(klass, query):
        if query == '':
            return []
        else:
            return klass.commandes().filter(nomPatient__contains=query)

