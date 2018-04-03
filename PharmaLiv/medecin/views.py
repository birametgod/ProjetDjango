from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from .forms import signUp,envoiOrdonnance
# Create your views here.
class reponse(FormView):
    template_name="medecin/reponse.html"
    form_class = envoiOrdonnance
    success_url ='/medecin/thanks/'
    #return render(request,'medecin/reponse.html')

def home(request):
    return render(request,'medecin/home.html')


class connexionView(FormView):
    template_name="medecin/formulaire.html"
    form_class = signUp
    success_url ='/medecin/thanks/'

    def form_valid(self,form):
        """This method is called when valid form data has been POSTed.
        It should return an HttpResponse."""
        user= form.save()
        login(self.request,user)
        return super().form_valid(form)

class envoiOrdannce(FormView):
    template_name="medecin/reponse.html"
    form_class = envoiOrdonnance
    success_url ='/medecin/thanks/'