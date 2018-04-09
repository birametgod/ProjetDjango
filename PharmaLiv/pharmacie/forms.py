from django import forms
from .models import Fiche_Produit
from .models import Pharmacie,Commandes_Effectuees
from connexion.models import User
from livreur.models import NotificationsLivreur
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget
from django.db import transaction



class EnvoiCommandeForm(forms.ModelForm):
	class Meta:
		model = NotificationsLivreur
		fields = '__all__'
		widgets = {
            'livreur' : forms.TextInput(attrs={'class':'form-control','placeholder':'livreur',}),
        }


class CreationFiche(forms.ModelForm):
	pharmacie=forms.IntegerField(required=True, label='')
	class Meta:
		model = Fiche_Produit
		fields = ('titre', 'photo', 'prix', 'description', 'types', 'categorie','stock')
		widgets = {
            'titre' : forms.TextInput(attrs={'class':'form-control','placeholder':'Titre',}),
            'prix' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Prix',}),
            'description' : forms.Textarea(attrs={'class':'form-control','placeholder':'Description',}),
            'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'Email',}),
			'types' :forms.TextInput(attrs={'class':'form-control','placeholder':'Types',}), 
        }

	def save(self):
		Fiche_Produit.objects.create(nom_id=self.cleaned_data.get('pharmacie'),titre=self.cleaned_data.get('titre'),photo=self.cleaned_data.get('photo'),prix=self.cleaned_data.get('prix'),description=self.cleaned_data.get('description'),types=self.cleaned_data.get('types'),categorie =self.cleaned_data.get('categorie'),stock=self.cleaned_data.get('stock'))



class CommandeForm(forms.ModelForm):
    	
		
		class Meta:
			"""
			il est possible de préciser quelques informations supplémentaires à Django via la classe Meta. 
			Celle-ci permet de préciser des comportements propres au modèle lui-même.

			"""
			model = Commandes_Effectuees
			fields = ('nomPatient','prenomPatient','email','adresse','telephonePatient','ordonnance','patient')
			widgets = {
				'nomPatient' : forms.TextInput(attrs={'class':'form-control','placeholder':'nom',}),
				'email' : forms.TextInput(attrs={'class':'form-control','placeholder':'Email',}),
				'patient' : forms.TextInput(attrs={'class':'form-control','placeholder':'patient',}),
			}
			
			


class signUp(UserCreationForm):
    	
		profil =forms.ImageField(widget=forms.ClearableFileInput(
 	       attrs={
 	           'class' : 'form-control',
 	       }
 	   ))
		adresse = forms.CharField(widget=forms.TextInput(
 	       attrs={
 	           'class' : 'form-control',
 	       }
 	   	))
		telephone = forms.IntegerField(required=True, label='Téléphone')
		horaire = forms.CharField(widget=forms.TextInput(
 	       attrs={
 	           'class' : 'form-control',
 	       }
 	   	))
		class Meta:
			"""
			il est possible de préciser quelques informations supplémentaires à Django via la classe Meta. 
			Celle-ci permet de préciser des comportements propres au modèle lui-même.

			"""
			model = User
			fields = ('username','email',)
			widgets = {
				'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'Nom',}),
				'email' : forms.TextInput(attrs={'class':'form-control','placeholder':'Email',}),
			}
			
			

		@transaction.atomic  #make sure those  operations are done in a single database transaction and avoid data inconsistencies in case of error.
		def save(self):
			user = super().save(commit=False) # Call the real save() method, modify what it's saving, it will do save(commit=False)
			user.is_pharmacie = True
			user.save()
			Pharmacie.objects.create(user=user,profil=self.cleaned_data.get('profil'),telephone=self.cleaned_data.get('telephone'),adresse=self.cleaned_data.get('adresse'),horaire=self.cleaned_data.get('horaire'))
			return user
		# TODO: Define form fields here