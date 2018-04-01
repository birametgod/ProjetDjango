from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from .forms import signUp
# Create your views here.
def reponse(request):
    return render(request,'pharmacie/reponse.html')

def home(request):
    return render(request,'pharmacie/home.html')


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
