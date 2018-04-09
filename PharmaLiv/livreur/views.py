from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from .forms import signUp
from .models import *
from pharmacie.models import Commandes_Effectuees

def reponse(request):
	Livreur.objects.filter(user_id=request.user.id).update(id=request.user.id),  
	context = {
		#'livreur': Livreur.objects.filter(livreur_id=request.user.id),
		#'notifications': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=False),
		#'nombreDeNotifications': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=False).count(),
		#'nbreMsg': NotificationsLivreur.objects.filter(livreur_id=request.user.id).count(),
	}
	return render(request, 'livreur/reponse.html', context)


def home(request):
	return render(request,'livreur/home.html')


class connexionView(FormView):
	template_name="livreur/newForm.html" #juste pour tester le formulaire de materialize bootstrap
	form_class = signUp
	success_url ='/livreur/thanks/'

	def form_valid(self,form):
		"""This method is called when valid form data has been POSTed.
		It should return an HttpResponse."""
		user= form.save()
		login(self.request,user)
		return super().form_valid(form)