from django import forms
from .models import Fiche_Produit
from .models import Pharmacie

class CreationFiche(forms.ModelForm):

    class Meta:
        model = Fiche_Produit
        fields = ('titre', 'photo', 'prix', 'description', 'types', )


class signUp(forms.ModelForm):

	class Meta: 
		model = Pharmacie
		fields = ('nom', 'adresse', 'telephone', 'horaire', 'login', 'password', 'profil', )

