from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from .forms import signUp
from .models import *
# Create your views here.
def reponse(request):
    context = {
        'notifications': Commandes_Effectuees.objects.filter(livree=0).count(), 
        'livrees': Commandes_Effectuees.objects.filter(livree=1),
        'nonlivrees': Commandes_Effectuees.objects.filter(livree=0),
        }
    return render(request,'pharmacie/reponse.html', context)

def home(request):
    return render(request,'pharmacie/home.html')

def partenaire(request):
    context = { 
        'notifications': Commandes_Effectuees.objects.filter(livree=0).count(), 
        'partenaires': Pharmacie.objects.raw('SELECT * FROM pharmacie_pharmacie where partenaire=1')
    }
    return render(request, 'pharmacie/acceuil_pharma.html', context)

def nonpartenaire(request):
    context = {
        'nonpartenaires': Pharmacie.objects.raw('SELECT * FROM pharmacie_pharmacie where partenaire=0')
    }
    return render(request, 'pharmacie/nonpartenaire.html', context)

class connexionView(FormView):
    template_name="pharmacie/formulaire.html"
    form_class = signUp
    success_url ='/pharmacie/thanks/'

    def form_valid(self,form):
        """This method is called when valid form data has been POSTed.
        It should return an HttpResponse."""
        user= form.save()
        login(self.request,user)
        return super().form_valid(form)
