from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from .forms import signUp,CreationFiche
from .models import *
# Create your views here.


class reponse(FormView):
    template_name="pharmacie/reponse.html"
    form_class = CreationFiche
    success_url ='/pharmacie/thanks/'

    def get_context_data(self, **kwargs):
        
        context = super(reponse, self).get_context_data(**kwargs)
        context = {
            'pharmacie': Pharmacie.objects.get(id=self.request.user.id),
            'form':CreationFiche,
        }
        return context
    
    def form_valid(self,form):
        form.save()
        return super(reponse, self).form_valid(form)



def home(request):
    return render(request,'pharmacie/home.html')

def partenaire(request):
    context = { 
        'notifications': Commandes_Effectuees.objects.filter(livree=0).count(), 
        'partenaires': Pharmacie.objects.raw('SELECT * FROM pharmacie_pharmacie where partenaire=1'),
        'medoc': Fiche_Produit.objects.all()
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
