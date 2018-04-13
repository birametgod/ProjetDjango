from django import forms
from PharmaLiv import settings
from connexion.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget
from django.db import transaction
from livreur.models import Region


class signUp(UserCreationForm):
	class Meta:
		model = User
		fields = ('username',)
		widgets = {
			'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'Login',}),
		}


	@transaction.atomic  #make sure those  operations are done in a single database transaction and avoid data inconsistencies in case of error.
	def save(self):
		user = super().save(commit=False) # Call the real save() method, modify what it's saving, it will do save(commit=False)
		user.is_userbi = True
		user.save()
		return user


class regionForm(forms.ModelForm):
	class Meta:
		model = Region
		fields = '__all__'