from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from .panier import Panier
from .forms import form_panier
from pharmacie.models import Fiche_Produit
# Create your views here.
@require_POST
def add_panier(request,id):
    panier = Panier(request)
    produit = Fiche_Produit.objects.get(id=id)
    form = form_panier(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        panier.add(produit=produit,stock=cd['quantite'],update_stock=cd['update'])
    return redirect('panier_detail')
        

def supprimer_panier(request,id):
    panier = Panier(request)
    produit = Fiche_Produit.objects.get(id=id)
    panier.remove(produit)
    return redirect('panier_detail')

def panier_detail(request):
    panier = Panier(request)
    return render(request,'payementLigne/panier.html',{'panier':panier})