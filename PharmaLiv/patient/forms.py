from django import forms
from .models import userbi
from django.contrib.admin.widgets import AdminDateWidget
class userbiForm(forms.ModelForm):
    """Form definition for Muserbi"""

    class Meta:
        """Meta definition for Muserbiorm."""

        model = userbi
        fields = ('user', 'bio', 'location', 'birth_date')

class signUp(forms.Form):
    """signUp definition."""
    login = forms.CharField(max_length=32, label='login',required=True)
    email = forms.CharField(max_length=32, label='email',required=True,widget = forms.EmailInput()) 
    password = forms.CharField(max_length=32, label='password',required=True,widget = forms.PasswordInput())
    bio = forms.CharField(max_length=155, label='bio',required=True)
    location = forms.CharField(max_length=32, label='location',required=True)
    birth_date = forms.DateField(required=True)

    # TODO: Define form fields here
 