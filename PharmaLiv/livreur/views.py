from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from .forms import signUp
from .models import *
from pharmacie.models import Commandes_Effectuees
from sample.forms import SampleForm
from patient.models import Patient
from sample.forms import SampleForm
from django.shortcuts import render, redirect


class SampleFormView(FormView):
    template_name = "livreur/reponse.html"
    form_class = SampleForm

    def get_context_data(self, **kwargs):
        Livreur.objects.filter(user_id=self.request.user.id).update(id=self.request.user.id),

        context = super(SampleFormView, self).get_context_data(**kwargs)
        context = {
            'form': SampleForm,
            'livreur': Livreur.objects.filter(user_id=self.request.user.id),
            'notificationsNonLu': NotificationsLivreur.objects.filter(livreur_id=self.request.user.id).filter(lu=False),
            'notificationsLu': NotificationsLivreur.objects.filter(livreur_id=self.request.user.id).filter(lu=True),
            'nombreDeNotifications': NotificationsLivreur.objects.filter(livreur_id=self.request.user.id).filter(lu=False).count(),
            'nbreMsg': NotificationsLivreur.objects.filter(livreur_id=self.request.user.id).count(),
            'livraison': NotificationsLivreur.objects.filter(livreur_id=self.request.user.id, livree=False),
            'nblivraison': NotificationsLivreur.objects.filter(livreur_id=self.request.user.id, livree=False).count(),
        }
        return context


def reponse(request):
    Livreur.objects.filter(user_id=request.user.id).update(id=request.user.id),
    context = {
        'livreur': Livreur.objects.filter(user_id=request.user.id),
        'notificationsNonLu': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=False),
        'notificationsLu': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=True),
        'nombreDeNotifications': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=False).count(),
        'nbreMsg': NotificationsLivreur.objects.filter(livreur_id=request.user.id).count(),
        'livraison': NotificationsLivreur.objects.filter(livreur_id=request.user.id, livree=False),
        'nblivraison': NotificationsLivreur.objects.filter(livreur_id=request.user.id, livree=False).count(),
        # livreur': Livreur.objects.filter(livreur_id=request.user.id),
        # 'notifications': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=False),
        # 'nombreDeNotifications': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=False).count(),
        # 'nbreMsg': NotificationsLivreur.objects.filter(livreur_id=request.user.id).count(),
    }
    return render(request, 'livreur/reponse.html', context)


def home(request):
    return render(request, 'livreur/home.html')


def MisAjourNotif(request, id):
    context = {
        'livreur': Livreur.objects.filter(user_id=request.user.id),
        'notificationsNonLu': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=False),
        'notificationsLu': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=True),
        'nombreDeNotifications': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=False).count(),
        'nbreMsg': NotificationsLivreur.objects.filter(livreur_id=request.user.id).count(),
        'livraison': NotificationsLivreur.objects.filter(livreur_id=request.user.id, livree=False),
        'nblivraison': NotificationsLivreur.objects.filter(livreur_id=request.user.id, livree=False).count(),
        'notif': NotificationsLivreur.objects.filter(id=id).update(lu=True),
    }

    return render(request, 'livreur/reponse.html', context)


def MisAjourCmd(request, id, idp):
    context = {
        'livreur': Livreur.objects.filter(user_id=request.user.id),
        'notificationsNonLu': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=False),
        'notificationsLu': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=True),
        'nombreDeNotifications': NotificationsLivreur.objects.filter(livreur_id=request.user.id).filter(lu=False).count(),
        'nbreMsg': NotificationsLivreur.objects.filter(livreur_id=request.user.id).count(),
        'livraison': NotificationsLivreur.objects.filter(livreur_id=request.user.id, livree=False),
        'nblivraison': NotificationsLivreur.objects.filter(livreur_id=request.user.id, livree=False).count(),
        'notif': NotificationsLivreur.objects.filter(id=id).update(lu=True),
        'cmd': NotificationsLivreur.objects.filter(id=id).update(livree=True),
        'cmdlivree': Commandes_Effectuees.objects.filter(patient_id=idp).update(livree=True)
    }

    return render(request, 'livreur/reponse.html', context)


class connexionView(FormView):
    # juste pour tester le formulaire de materialize bootstrap
    template_name = "livreur/newForm.html"
    form_class = signUp
    success_url = '/livreur/thanks/'

    def form_valid(self, form):
        """This method is called when valid form data has been POSTed.
        It should return an HttpResponse."""
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
