from django import forms
from PharmaLiv import settings
from .models import *
from connexion.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget
from django.db import transaction


class signUp(UserCreationForm):
    """
    UserCreationForm, which defines the username and password fields
    """
    dateNaissance = forms.DateField (input_formats=settings.DATE_INPUT_FORMATS, required=True, label="Date de Naissance")
    telephone = forms.IntegerField(required=True, label='Téléphone')
    #CHOICES = Specialite.objects.all().values()
    specialite =forms.ChoiceField(choices=[(choice.pk, choice.nom) for choice in Specialite.objects.all()], label="Spécialité")
    hopital = forms.CharField(max_length=30, required=True, label='Hopital')

    class Meta:
        """
        il est possible de préciser quelques informations supplémentaires à Django via la classe Meta. 
        Celle-ci permet de préciser des comportements propres au modèle lui-même.

        """
        model = User
        fields = ('username','first_name','last_name','email',)
        
        

    @transaction.atomic  #make sure those  operations are done in a single database transaction and avoid data inconsistencies in case of error.
    def save(self):
        user = super().save(commit=False) # Call the real save() method, modify what it's saving, it will do save(commit=False)
        user.is_medecin = True
        user.save()
        Medecin.objects.create(user=user,dateNaissance=self.cleaned_data.get('dateNaissance'),telephone=self.cleaned_data.get('telephone'),specialite_id=self.cleaned_data.get('specialite'),hopital=self.cleaned_data.get('hopital'))
        return user
    # TODO: Define form fields here



