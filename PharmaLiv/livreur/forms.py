from django import forms
from PharmaLiv import settings
from livreur.models import Region,Livreur
from connexion.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget
from django.db import transaction

class signUp(UserCreationForm):
	sexes = (
		('homme', 'M'),
		('femme', 'F'),
	)
	regions = (
		('dakar', 'Dakar'),
		('thies', 'Thiès'),
	)

	sexe = forms.ChoiceField(choices=sexes)
	dateNaissance =forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
	telephone = forms.IntegerField()
	adresse = forms.CharField(widget=forms.TextInput(
		attrs={
			'class' : 'form-control',
			'placeholder' : 'Adresse',
		}
	))
	zoneDeLivraison = forms.ChoiceField(choices=[(choice.id, choice.zoneDeLivraison) for choice in Region.objects.all()])

	class Meta:
		"""
		il est possible de préciser quelques informations supplémentaires à Django via la classe Meta. 
		Celle-ci permet de préciser des comportements propres au modèle lui-même.

		"""
		model = User
		fields = ('username','first_name','last_name',)
		widgets = {
			'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'Login',}),
			'first_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Prénom',}),
			'last_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Nom',}),
		}


	@transaction.atomic  #make sure those  operations are done in a single database transaction and avoid data inconsistencies in case of error.
	def save(self):
		user = super().save(commit=False) # Call the real save() method, modify what it's saving, it will do save(commit=False)
		user.is_livreur = True
		user.save()
		Livreur.objects.create(user=user,sexe=self.cleaned_data.get('sexe'),
			adresse=self.cleaned_data.get('adresse'),
			dateNaissance=self.cleaned_data.get('dateNaissance'),telephone=self.cleaned_data.get('telephone'),
			zoneDeLivraison_id=self.cleaned_data.get('zoneDeLivraison'))
		return user
