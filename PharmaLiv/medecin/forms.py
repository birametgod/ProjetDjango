from django import forms
from PharmaLiv import settings
from .models import *
from patient.models import Ordonnances,Patient
from connexion.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget
from django.db import transaction

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)

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

class envoiOrdonnance(forms.Form):
    """Form definition for MODELNAME."""
    libelle = forms.CharField(widget=forms.Textarea(
        attrs={
            'class' : 'form-control',
            'placeholder' : "Ecrire l'ordonnance ",
        }
    ))
    medecin=forms.IntegerField(required=True, label='Téléphone')
    #medecin= forms.CharField(widget=forms.TextInput(
    #    attrs={
    #        'class' : 'form-control',
    #        'placeholder' : "medecin ",
    #    }
    #))

    medicaments = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={
            'class' : 'form-control',
        }
    ))
    patient =forms.ChoiceField(choices= [(choice.pk, choice.user.username) for choice in Patient.objects.all()])
    birth_date = forms.DateField(widget=forms.SelectDateWidget( empty_label=("Choose Year", "Choose Month", "Choose Day"),),)
    
    #make sure those  operations are done in a single database transaction and avoid data inconsistencies in case of error.
    def save(self):
        id=self.cleaned_data.get('medecin')
        Medecin.objects.filter(user_id=id).update(id=id)
        Ordonnances.objects.create(libelle=self.cleaned_data.get('libelle'),medicaments=self.cleaned_data.get('medicaments'),patient_id=self.cleaned_data.get('patient'),dateSoumission=self.cleaned_data.get('birth_date'),medecin_id=id)
        

    




