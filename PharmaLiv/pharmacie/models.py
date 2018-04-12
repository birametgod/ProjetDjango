from django.db import models
from django.utils.text import slugify
from PharmaLiv import settings
from patient.models import Patient
# Create your models here.

paiement= (
		('Wari', 'Wari'),
		('Orange Money', 'Orange Money'),
		('Carte de credit', 'Carte de credit'),
		)

class Pharmacie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    profil = models.ImageField(default='pharmacie.jpg', blank=True)
    adresse = models.CharField(max_length=100, null=False)
    telephone = models.IntegerField(max_length=9, null=False)
    horaire = models.CharField(max_length=50, null=False)
    partenaire = models.BooleanField(default="1")
    slug = models.SlugField()

    def __str__(self):
        return self.adresse

    def _get_unique_slug(self):
        slug = slugify(self.adresse)
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


class Categorie(models.Model):
    nom = models.CharField(max_length=200,)
    slug = models.SlugField()

    def __str__(self):
        return self.nom

    def _get_unique_slug(self):
        slug = slugify(self.nom)
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


class Fiche_Produit(models.Model):
    titre = models.CharField(max_length=50, null=False)
    photo = models.ImageField(default='default.jpg', blank=True)
    prix = models.IntegerField(max_length=10, null=False)
    description = models.TextField(max_length=200, default='DESC', null=False)
    types = models.CharField(max_length=10, default='Pharmacie', null=False)
    nom = models.ForeignKey(Pharmacie, on_delete=models.CASCADE, null=False)
    categorie = models.ForeignKey(
        Categorie, on_delete=models.CASCADE, null=False)
    stock = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    slug = models.SlugField()

    def __str__(self):
        return self.titre

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
    def publiees(cls):
        return cls.objects.all().order_by('prix')

    @classmethod
    def liste_publiees(cls,request):
        return cls.publiees().filter(nom_id=request.user.id)

    @classmethod
    def search(klass, query):
        if query == '':
            return []
        else:
            return klass.liste_publiees().filter(titre__contains=query)


class Commandes_Effectuees(models.Model):
    nomPatient = models.CharField(max_length=30, null=False)
    prenomPatient = models.CharField(max_length=30, null=False)
    adresse = models.CharField(max_length=100, null=False)
    telephonePatient = models.IntegerField(max_length=9, null=False)
    dateCommande = models.DateTimeField(
        auto_now_add=True, auto_now=False, verbose_name="Date de la commande", null=False)
    dateLivraison = models.DateTimeField(
        auto_now_add=True, auto_now=False, verbose_name="Date de livrason", null=False)
    livree = models.BooleanField(default=False)
    slug = models.SlugField()
    ordonnance = models.ImageField(default='default.jpg', blank=True)
    email = models.EmailField(max_length=100, null=False)
    payer = models.CharField(max_length=100, choices = paiement)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    lu = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s %s ' % (self.nomPatient, self.prenomPatient, self.dateCommande)

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


class detail_commande(models.Model):
    commande = models.ForeignKey(
        Commandes_Effectuees, on_delete=models.CASCADE)
    produit = models.ForeignKey(Fiche_Produit, on_delete=models.CASCADE)
    prix = models.IntegerField(max_length=10, null=False)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.prix
