from django.shortcuts import render
from patient.models import *
from medecin.models import *
from livreur.models import *
from pharmacie.models import *
# Create your views here.

def reponse(request):
	Userbi.objects.filter(user_id=request.user.id).update(id=request.user.id),  
	context = {
		'patient': Patient.objects.all(),
		'nbrePatient': Patient.objects.all().count(),
		'nbrePatienthomme': Patient.objects.filter(sexe='homme').count(),
		'nbrePatientfemme': Patient.objects.filter(sexe='femme').count(),
		'nbrePatientOrdonnances': Ordonnances.objects.filter().count(),
		'livreur': Livreur.objects.all(),
		'nbreLivreur': Livreur.objects.all().count(),
		'pharmacie': Pharmacie.objects.all(),
		'nbrePharmacie': Pharmacie.objects.all().count(),
		'medecin': Medecin.objects.all(),
		'nbreMedecin': Medecin.objects.all().count(),  
		'nbreFicheProduit': Fiche_produit.objects.all().count(),
		'nbreDeMedocPharma': Fiche_produit.objects.filter(types='Pharmacie').count(),
		'nbreMedocParapharma': Fiche_produit.objects.filter(types='Parapharmacie').count(),
		'nbreMedocVendu': NotificationsLivreur.objects.filter(livree=1).count(),
	}
	return render(request, 'userAdmin/reponse.html', context)


def home(request):
	return render(request,'userAdmin/reponse.html')