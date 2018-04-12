from django.shortcuts import render, redirect
from patient.models import *
from medecin.models import *
from livreur.models import *
from pharmacie.models import Pharmacie
from .models import userAdmin
from .forms import signUp, regionForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from connexion.models import User
import datetime
# Create your views here.

def reponse(request):
	#Userbi.objects.filter(user_id=request.user.id).update(id=request.user.id),  
	context = {
		
	}
	return render(request, 'userAdmin/reponse.html', context)


def home(request):
	context={
		#Patient
		'patient' : Patient.objects.all(),
		'nbrpatient' : Patient.objects.all().count(),

		'nbrpatientJanv' : User.objects.filter(date_joined__gt=datetime.date(2017, 12, 31), date_joined__lt=datetime.date(2018, 1, 31), is_patient=1).count(),
		'nbrpatientFev' : User.objects.filter(date_joined__gt=datetime.date(2018, 1, 31), date_joined__lt=datetime.date(2018, 3, 1), is_patient=1).count(),
		'nbrpatientMars' : User.objects.filter(date_joined__gt=datetime.date(2018, 3, 1), date_joined__lt=datetime.date(2018, 4, 1), is_patient=1).count(),
		'nbrpatientAvril' : User.objects.filter(date_joined__gt=datetime.date(2018, 4, 1), date_joined__lt=datetime.date(2018, 5, 1), is_patient=1).count(),
		'nbrpatientMai' : User.objects.filter(date_joined__gt=datetime.date(2018, 5, 1), date_joined__lt=datetime.date(2018, 6, 1), is_patient=1).count(),
		'nbrpatientJuin' : User.objects.filter(date_joined__gt=datetime.date(2018, 6, 1), date_joined__lt=datetime.date(2018, 7, 1), is_patient=1).count(),
		'nbrpatientJuil' : User.objects.filter(date_joined__gt=datetime.date(2018, 7, 1), date_joined__lt=datetime.date(2018, 8, 1), is_patient=1).count(),
		'nbrpatientAout' : User.objects.filter(date_joined__gt=datetime.date(2018, 8, 1), date_joined__lt=datetime.date(2018, 9, 1), is_patient=1).count(),
		'nbrpatientSept' : User.objects.filter(date_joined__gt=datetime.date(2018, 9, 1), date_joined__lt=datetime.date(2018, 10, 1), is_patient=1).count(),
		'nbrpatientOct' : User.objects.filter(date_joined__gt=datetime.date(2018, 10, 1), date_joined__lt=datetime.date(2018, 11, 1), is_patient=1).count(),
		'nbrpatientNov' : User.objects.filter(date_joined__gt=datetime.date(2018, 11, 1), date_joined__lt=datetime.date(2018, 12, 1), is_patient=1).count(),
		'nbrpatientDec' : User.objects.filter(date_joined__gt=datetime.date(2018, 12, 1), date_joined__lt=datetime.date(2018, 12, 31), is_patient=1).count(),
		
		'nbrpatientHomme' : Patient.objects.filter(sexe='Homme').count(),
		'nbrpatientFemme' : Patient.objects.filter(sexe='Femme').count(),
		'nbrpatientTotal': Patient.objects.all().count(),

		#Pharmacie
		'pharmacie' : Pharmacie.objects.all(),
		'nbrpharmacie' : Pharmacie.objects.all().count(),

		'nbrpharmaJanv' : User.objects.filter(date_joined__gt=datetime.date(2017, 12, 31), date_joined__lt=datetime.date(2018, 1, 31), is_pharmacie=1).count(),
		'nbrpharmaFev' : User.objects.filter(date_joined__gt=datetime.date(2018, 1, 31), date_joined__lt=datetime.date(2018, 3, 1), is_pharmacie=1).count(),
		'nbrpharmaMars' : User.objects.filter(date_joined__gt=datetime.date(2018, 3, 1), date_joined__lt=datetime.date(2018, 4, 1), is_pharmacie=1).count(),
		'nbrpharmaAvril' : User.objects.filter(date_joined__gt=datetime.date(2018, 4, 1), date_joined__lt=datetime.date(2018, 5, 1), is_pharmacie=1).count(),
		'nbrpharmaMai' : User.objects.filter(date_joined__gt=datetime.date(2018, 5, 1), date_joined__lt=datetime.date(2018, 6, 1), is_pharmacie=1).count(),
		'nbrpharmaJuin' : User.objects.filter(date_joined__gt=datetime.date(2018, 6, 1), date_joined__lt=datetime.date(2018, 7, 1), is_pharmacie=1).count(),
		'nbrpharmaJuil' : User.objects.filter(date_joined__gt=datetime.date(2018, 7, 1), date_joined__lt=datetime.date(2018, 8, 1), is_pharmacie=1).count(),
		'nbrpharmaAout' : User.objects.filter(date_joined__gt=datetime.date(2018, 8, 1), date_joined__lt=datetime.date(2018, 9, 1), is_pharmacie=1).count(),
		'nbrpharmaSept' : User.objects.filter(date_joined__gt=datetime.date(2018, 9, 1), date_joined__lt=datetime.date(2018, 10, 1), is_pharmacie=1).count(),
		'nbrpharmaOct' : User.objects.filter(date_joined__gt=datetime.date(2018, 10, 1), date_joined__lt=datetime.date(2018, 11, 1), is_pharmacie=1).count(),
		'nbrpharmaNov' : User.objects.filter(date_joined__gt=datetime.date(2018, 11, 1), date_joined__lt=datetime.date(2018, 12, 1), is_pharmacie=1).count(),
		'nbrpharmaDec' : User.objects.filter(date_joined__gt=datetime.date(2018, 12, 1), date_joined__lt=datetime.date(2018, 12, 31), is_pharmacie=1).count(),
		
		#Medecin
		'medecin' : Medecin.objects.all(),
		'nbrmedecin' : Medecin.objects.all().count(),

		'nbrmedJanv' : User.objects.filter(date_joined__gt=datetime.date(2017, 12, 31), date_joined__lt=datetime.date(2018, 1, 31), is_medecin=1).count(),
		'nbrmedFev' : User.objects.filter(date_joined__gt=datetime.date(2018, 1, 31), date_joined__lt=datetime.date(2018, 3, 1), is_medecin=1).count(),
		'nbrmedMars' : User.objects.filter(date_joined__gt=datetime.date(2018, 3, 1), date_joined__lt=datetime.date(2018, 4, 1), is_medecin=1).count(),
		'nbrmedAvril' : User.objects.filter(date_joined__gt=datetime.date(2018, 4, 1), date_joined__lt=datetime.date(2018, 5, 1), is_medecin=1).count(),
		'nbrmedMai' : User.objects.filter(date_joined__gt=datetime.date(2018, 5, 1), date_joined__lt=datetime.date(2018, 6, 1), is_medecin=1).count(),
		'nbrmedJuin' : User.objects.filter(date_joined__gt=datetime.date(2018, 6, 1), date_joined__lt=datetime.date(2018, 7, 1), is_medecin=1).count(),
		'nbrmedJuil' : User.objects.filter(date_joined__gt=datetime.date(2018, 7, 1), date_joined__lt=datetime.date(2018, 8, 1), is_medecin=1).count(),
		'nbrmedAout' : User.objects.filter(date_joined__gt=datetime.date(2018, 8, 1), date_joined__lt=datetime.date(2018, 9, 1), is_medecin=1).count(),
		'nbrmedSept' : User.objects.filter(date_joined__gt=datetime.date(2018, 9, 1), date_joined__lt=datetime.date(2018, 10, 1), is_medecin=1).count(),
		'nbrmedOct' : User.objects.filter(date_joined__gt=datetime.date(2018, 10, 1), date_joined__lt=datetime.date(2018, 11, 1), is_medecin=1).count(),
		'nbrmedNov' : User.objects.filter(date_joined__gt=datetime.date(2018, 11, 1), date_joined__lt=datetime.date(2018, 12, 1), is_medecin=1).count(),
		'nbrmedDec' : User.objects.filter(date_joined__gt=datetime.date(2018, 12, 1), date_joined__lt=datetime.date(2018, 12, 31), is_medecin=1).count(),
		
		'nbrmedDent' : Medecin.objects.filter(specialite_id=1).count(),
		'nbrmedGyn' : Medecin.objects.filter(specialite_id=2).count(),
		'nbrmedOph' : Medecin.objects.filter(specialite_id=3).count(),
		'nbrmedDer' : Medecin.objects.filter(specialite_id=4).count(),
		'nbrmedPsy' : Medecin.objects.filter(specialite_id=5).count(),
		'nbrmedChir' : Medecin.objects.filter(specialite_id=6).count(),
		'nbrmedPed' : Medecin.objects.filter(specialite_id=7).count(),

		#Livreur
		'livreur' : Livreur.objects.all(),
		'nbrlivreur' : Livreur.objects.all().count(),


		'nbrpatJanv' : User.objects.filter(date_joined__gt=datetime.date(2017, 12, 31), date_joined__lt=datetime.date(2018, 1, 31), is_patient=1).count(),
		'nbrpatFev' : User.objects.filter(date_joined__gt=datetime.date(2018, 1, 31), date_joined__lt=datetime.date(2018, 3, 1), is_patient=1).count(),
		'nbrpatMars' : User.objects.filter(date_joined__gt=datetime.date(2018, 3, 1), date_joined__lt=datetime.date(2018, 4, 1), is_patient=1).count(),
		'nbrpatAvril' : User.objects.filter(date_joined__gt=datetime.date(2018, 4, 1), date_joined__lt=datetime.date(2018, 5, 1), is_patient=1).count(),
		'nbrpatMai' : User.objects.filter(date_joined__gt=datetime.date(2018, 5, 1), date_joined__lt=datetime.date(2018, 6, 1), is_patient=1).count(),
		'nbrpatJuin' : User.objects.filter(date_joined__gt=datetime.date(2018, 6, 1), date_joined__lt=datetime.date(2018, 7, 1), is_patient=1).count(),
		'nbrpatJuil' : User.objects.filter(date_joined__gt=datetime.date(2018, 7, 1), date_joined__lt=datetime.date(2018, 8, 1), is_patient=1).count(),
		'nbrpatAout' : User.objects.filter(date_joined__gt=datetime.date(2018, 8, 1), date_joined__lt=datetime.date(2018, 9, 1), is_patient=1).count(),
		'nbrpatSept' : User.objects.filter(date_joined__gt=datetime.date(2018, 9, 1), date_joined__lt=datetime.date(2018, 10, 1), is_patient=1).count(),
		'nbrpatOct' : User.objects.filter(date_joined__gt=datetime.date(2018, 10, 1), date_joined__lt=datetime.date(2018, 11, 1), is_patient=1).count(),
		'nbrpatNov' : User.objects.filter(date_joined__gt=datetime.date(2018, 11, 1), date_joined__lt=datetime.date(2018, 12, 1), is_patient=1).count(),
		'nbrpatDec' : User.objects.filter(date_joined__gt=datetime.date(2018, 12, 1), date_joined__lt=datetime.date(2018, 12, 31), is_patient=1).count(),
		
		'nbrlivzone1':Livreur.objects.filter(zoneDeLivraison_id=1).count(),
		'nbrlivzone2':Livreur.objects.filter(zoneDeLivraison_id=2).count(),
		'nbrlivzone3':Livreur.objects.filter(zoneDeLivraison_id=3).count(),
		'nbrlivzone4':Livreur.objects.filter(zoneDeLivraison_id=4).count(),
		'nbrlivzone5':Livreur.objects.filter(zoneDeLivraison_id=5).count(),
	}
	return render(request,'userAdmin/reponse.html', context)


class connexionView(FormView):
	template_name="userAdmin/formulaire.html" #juste pour tester le formulaire de materialize bootstrap
	form_class = signUp
	success_url ='/userAdmin/thanks/'

	def form_valid(self,form):
		"""This method is called when valid form data has been POSTed.
		It should return an HttpResponse."""
		user= form.save()
		login(self.request,user)
		return super().form_valid(form)
	

def zone(request):
	form = regionForm(request.POST or None)
	if form.is_valid(): 
		zoneDeLivraison = form.cleaned_data['zoneDeLivraison']
		region = form.cleaned_data['region']
		envoi = True
		form.save()
	return render(request, 'userAdmin/reponse.html', locals())

