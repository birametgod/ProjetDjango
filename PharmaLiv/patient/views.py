from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import signUp
from .models import userbi
# Create your views here.
def reponse(request):
     return render (request,'patient/reponse.html')

def showUser(request):
    formulaire = signUp()
    context = {
        'formulaire':formulaire
    }
    if request.method=='POST':
        formulaire = signUp(request.POST)
        if formulaire.is_valid():
            userr = formulaire.cleaned_data
            username = userr['login']
            email = userr['email']
            password=userr['password']
            bio = userr['bio']
            location=userr['location']
            birth_date=userr['birth_date']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                user = User.objects.create_user(username,email,password)
                profil = userbi(user=user,bio=bio,location=location,birth_date=birth_date)
                profil.save()
                aut = authenticate(username = username, password = password)
                login(request, aut)
                return HttpResponseRedirect('thanks/')

            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
            
    else:
        return render (request,'patient/formulaire.html', context)
            
        