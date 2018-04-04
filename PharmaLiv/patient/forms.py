from django import forms
from PharmaLiv import settings
from .models import Patient
from connexion.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget
from django.db import transaction


class signUp(UserCreationForm):
    """
    UserCreationForm, which defines the username and password fields
    """

    allergie = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Allergie',
        }
    ))
    sexes = (
        ('homme', 'M'),
        ('femme', 'F'),
    )
    sexe = forms.ChoiceField(choices=sexes)
    #allergie = forms.CharField( max_length=32, label='allergie',required=True)
    traitement = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Traitement',
        }
    ))
    
    dateNaissance =forms.DateField (input_formats=settings.DATE_INPUT_FORMATS)
    adresse = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Adresse',
        }
    ))

    class Meta:
        """
        il est possible de préciser quelques informations supplémentaires à Django via la classe Meta. 
        Celle-ci permet de préciser des comportements propres au modèle lui-même.

        """
        model = User
        fields = ('username','first_name','last_name','email','password',)
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'Login',}),
            'first_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Prénom',}),
            'password' : forms.PasswordInput(attrs={'class':'form-control','placeholder':'Mot de passe',}), 
            'last_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Nom',}),
            'email' : forms.TextInput(attrs={'class':'form-control','placeholder':'Email',}),


        }
        
        

    @transaction.atomic  #make sure those  operations are done in a single database transaction and avoid data inconsistencies in case of error.
    def save(self):
        user = super().save(commit=False) # Call the real save() method, modify what it's saving, it will do save(commit=False)
        user.is_patient = True
        user.save()
        Patient.objects.create(user=user,sexe=self.cleaned_data.get('sexe'),allergie=self.cleaned_data.get('allergie'),traitement=self.cleaned_data.get('traitement'),dateNaissance=self.cleaned_data.get('dateNaissance'),adresse=self.cleaned_data.get('adresse'))
        return user
    # TODO: Define form fields here
