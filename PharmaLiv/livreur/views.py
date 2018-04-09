from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from .forms import signUp
from .models import *
from pharmacie.models import Commandes_Effectuees

def reponse(request):
	Livreur.objects.filter(user_id=request.user.id).update(id=request.user.id),  
	context = {
<<<<<<< HEAD
		'livreur': Livreur.objects.filter(user_id=request.user.id),
		'notificationsNonLu': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=False),
		'notificationsLu': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=True),
		'nombreDeNotifications': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=False).count(),
		'nbreMsg': NotificationsLivreur.objects.filter(livreur_id=request.user.id).count(),
		'livraison':NotificationsLivreur.objects.filter(livreur_id=request.user.id, livree=False),
		'nblivraison':NotificationsLivreur.objects.filter(livreur_id=request.user.id, livree=False).count(),
=======
		#livreur': Livreur.objects.filter(livreur_id=request.user.id),
		#'notifications': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=False),
		#'nombreDeNotifications': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=False).count(),
		#'nbreMsg': NotificationsLivreur.objects.filter(livreur_id=request.user.id).count(),
>>>>>>> 8ae81be8a6b171dfaaff95463560bda9eaa11879
	}
	return render(request, 'livreur/reponse.html', context)


def home(request):
	return render(request,'livreur/home.html')


def MisAjourNotif(request, id):
	context={
		'livreur': Livreur.objects.filter(user_id=request.user.id),
		'notificationsNonLu': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=False),
		'notificationsLu': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=True),
		'nombreDeNotifications': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=False).count(),
		'nbreMsg': NotificationsLivreur.objects.filter(livreur_id=request.user.id).count(),
		'livraison':NotificationsLivreur.objects.filter(livreur_id=request.user.id, livree=False),
		'nblivraison':NotificationsLivreur.objects.filter(livreur_id=request.user.id, livree=False).count(),
		'notif' : NotificationsLivreur.objects.filter(id=id).update(lu=True),
	}
	
	return render(request, 'livreur/reponse.html',context)

def MisAjourCmd(request, id):
	context={
		'livreur': Livreur.objects.filter(user_id=request.user.id),
		'notificationsNonLu': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=False),
		'notificationsLu': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=True),
		'nombreDeNotifications': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=False).count(),
		'nbreMsg': NotificationsLivreur.objects.filter(livreur_id=request.user.id).count(),
		'livraison':NotificationsLivreur.objects.filter(livreur_id=request.user.id, livree=False),
		'nblivraison':NotificationsLivreur.objects.filter(livreur_id=request.user.id, livree=False).count(),
		'notif' : NotificationsLivreur.objects.filter(id=id).update(lu=True),
		'cmd' : NotificationsLivreur.objects.filter(id=id).update(livree=True),
		#'cmdlivree' : Commandes_Effectuees.objects.filter(patient_id).update(livree=True)
	}
	
	return render(request, 'livreur/reponse.html',context)


class connexionView(FormView):
	template_name="livreur/formulaire.html" #juste pour tester le formulaire de materialize bootstrap
	form_class = signUp
	success_url ='/livreur/thanks/'

	def form_valid(self,form):
		"""This method is called when valid form data has been POSTed.
		It should return an HttpResponse."""
		user= form.save()
		login(self.request,user)
		return super().form_valid(form)