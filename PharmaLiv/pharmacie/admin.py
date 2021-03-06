from django.contrib import admin
from .models import *

# Register your models here.

class PharmacieAdmin(admin.ModelAdmin):
	list_display = ('profil', 'user', 'adresse', 'telephone', 'horaire', )
	ordering = ('user', )


class Fiche_ProduitAdmin(admin.ModelAdmin):
	list_display = ('photo', 'titre', 'prix', 'types', 'nom', )
	ordering = ('nom', )

class Commandes_EffectueesAdmin(admin.ModelAdmin):
	list_display = ('nomPatient', 'prenomPatient', 'adresse', 'telephonePatient', 'dateCommande', 'dateLivraison', 'livree')
	ordering = ('livree', )



admin.site.register(Categorie)
admin.site.register(Pharmacie, PharmacieAdmin)
admin.site.register(Fiche_Produit, Fiche_ProduitAdmin)
admin.site.register(Commandes_Effectuees, Commandes_EffectueesAdmin)