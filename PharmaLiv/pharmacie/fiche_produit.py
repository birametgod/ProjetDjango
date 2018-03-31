from django import forms
from .models import Fiche_Produit


class CreationFiche(forms.ModelForm):

    class Meta:
        model = Fiche_Produit
        fields = ('titre', 'photo', 'prix', 'description', 'types',)