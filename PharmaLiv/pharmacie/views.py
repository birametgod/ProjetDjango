from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from .forms import signUp,CreationFiche,CommandeForm,EnvoiCommandeForm
from .models import *
from livreur.models import Livreur,NotificationsLivreur
from payementLigne.panier import Panier
from payementLigne.forms import form_panier
# Create your views here.


class reponse(FormView):
    template_name="pharmacie/reponse.html"
    form_class = CreationFiche
    success_url ='/pharmacie/thanks/'

    def get_context_data(self, **kwargs):
        
        context = super(reponse, self).get_context_data(**kwargs)
        context = {
            'pharmacie': Pharmacie.objects.get(id=self.request.user.id),
            'nonlivrees' : Commandes_Effectuees.objects.filter(livree=0), 
            'livrees' : Commandes_Effectuees.objects.filter(livree=1), 
            'form':CreationFiche,
            'notifications': Commandes_Effectuees.objects.filter(livree=0).count(), 
            'produit': Fiche_Produit.objects.filter(nom_id=self.request.user.id), 
            'l' : Livreur.objects.all()
        }
        return context
    
    def form_valid(self,form):
        form.save()
        return super(reponse, self).form_valid(form)


def livre_produit(request,id):
    formulaire = EnvoiCommandeForm()
    context ={
        'indicommande' : Livreur.objects.get(id=id),
        'form':formulaire,
    }
    if request.method == 'POST':
        form = EnvoiCommandeForm(request.POST)
        if form.is_valid():
            notif = NotificationsLivreur(**form.cleaned_data)
            notif.save()
            return render(request, 'pharmacie/livreur.html',context) 
    else:
        return render(request, 'pharmacie/livreur.html',context)


def home(request):
    return render(request,'pharmacie/home.html')

def comm_prod(request,id):
    context = {
        'produit' : detail_commande.objects.filter(commande_id = id),
        
    }
    return render(request,'pharmacie/comm.html',context)

def creer_commande(request):
    panier = Panier(request)
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            commande = form.save()
            for item in panier:
                detail_commande.objects.create(commande=commande,produit=item['produit'],prix=item['prix'],stock=item['stock'])
                panier.clear()
            return render(request,'payementLigne/cree.html',{'commande':commande})
    else:
        form = CommandeForm()
    return render(request,'payementLigne/commande.html',{'panier':panier,'form':form})


def detail(request,id):
    panierForm = form_panier()
    context = { 
        'medoc': Fiche_Produit.objects.get(id=id,disponible=True),
        'panier_form': panierForm,

    }
    return render(request, 'pharmacie/medicament.html', context)

def partenaire(request,id):
    context = { 
        
        'partenaires': Pharmacie.objects.raw('SELECT * FROM pharmacie_pharmacie where partenaire=1'),
        'medoc': Fiche_Produit.objects.filter(nom_id=id,disponible=True)
    }
    return render(request, 'pharmacie/pageEcom.html', context)

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
