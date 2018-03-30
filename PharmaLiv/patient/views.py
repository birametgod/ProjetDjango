from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import signUp
from .models import userbi
# Create your views here.

def showUser(request):
    formulaire = signUp()
    context = {
        'formulaire':formulaire
    }
    if request.method=='POST':
        formulaire = signUp(request.POST)
        if formulaire.is_valid():
            userr = formulaire.clean_data
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
            
    else:
        return render (request,'patient/formulaire.html', context)
            
        