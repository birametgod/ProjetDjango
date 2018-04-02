from django import forms
from .models import Fiche_Produit
from .models import Pharmacie
from connexion.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget
from django.db import transaction


class CreationFiche(forms.ModelForm):

	class Meta:
		model = Fiche_Produit
		fields = ('titre', 'photo', 'prix', 'description', 'types', )


class signUp(forms.ModelForm):
	profil = forms.ImageField()
	adresse = forms.CharField(max_length = 100, required=True, label='Adresse')
	telephone = forms.IntegerField(required=True, label='Téléphone')
	horaire = forms.CharField(max_length = 50, required=True, label='Horaire')


	class Meta: 
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', )



	@transaction.atomic  #make sure those  operations are done in a single database transaction and avoid data inconsistencies in case of error.
	def save(self):
		pharmacie = super().save(commit=False) # Call the real save() method, modify what it's saving, it will do save(commit=False)
		pharmacie.is_pharmacie = True
		pharmacie.save()
		Pharmacie.objects.create(user=pharmacie,profil=self.cleaned_data.get('profil'),telephone=self.cleaned_data.get('telephone'),adresse=self.cleaned_data.get('adresse'),horaire=self.cleaned_data.get('horaire'))
		return pharmacie