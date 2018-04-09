from django.urls import path,include
from . import views
from patient import views as patient_views
from pharmacie import views as pharmacie_views
from medecin import views as medecin_views
from livreur import views as livreur_views
from django.contrib.auth import views as auth_views

"""
from django.contrib.auth import views => classe de django qui nous donne des methode
pour nous permettre de gerer plus facilement la connexion et la deconnexion ...
"""

urlpatterns = [
    path('', views.home), 

    #conexion et deconnexion patient
    path('patient/', include([
        path('etat/', patient_views.reponseFemme.as_view()),
        path('notifications', patient_views.notification, name="notif"),
        path('', patient_views.home),
        path('inscription/', patient_views.connexionView.as_view()),
        path('thanks/', patient_views.reponse,name="afficher_reponse"),
        path('logout/', auth_views.logout,{'template_name':'connexion/home.html'},name='patient_deconn'),#.logout nous gere la deconnexion , meme pas besoin d'ecrire une methode dans views.py,il nous redirige directement dans le template_name
        path('login/', auth_views.login,{'template_name':'patient/login.html'}), #meme chose pour .login ,patient/login.html est la page pour se connecter , django nous gere la verification et nous redirige vers l'url indiqué dans input type hidden de la page html
    ])),

    #connexion et deconnexion pharmacie
    path('pharmacie/', include([
        path('', pharmacie_views.home),
        path('inscription/', pharmacie_views.connexionView.as_view()),
        path('thanks/', pharmacie_views.reponse,name="afficher_reponse"),
        path('logout/', auth_views.logout,{'template_name':'connexion/home.html'},name='pharmacie_deconn'),#.logout nous gere la deconnexion , meme pas besoin d'ecrire une methode dans views.py,il nous redirige directement dans le template_name
        path('login/', auth_views.login,{'template_name':'pharmacie/login.html'}), #meme chose pour .login ,patient/login.html est la page pour se connecter , django nous gere la verification et nous redirige vers l'url indiqué dans input type hidden de la page html
	    path('partenaire/', pharmacie_views.partenaire), 
	    path('nonpartenaire/', pharmacie_views.nonpartenaire),
    ])),

    #connexion et deconnexion medecin
    path('medecin/', include([
        path('', medecin_views.home),
        path('inscription/', medecin_views.connexionView.as_view()),
        path('thanks/', medecin_views.reponse.as_view(),name="afficher_reponse"),
        path('logout/', auth_views.logout,{'template_name':'medecin/home.html',},name='medecin_deconn'),#.logout nous gere la deconnexion , meme pas besoin d'ecrire une methode dans views.py,il nous redirige directement dans le template_name
        path('login/', auth_views.login,{'template_name':'medecin/login.html'}), #meme chose pour .login ,patient/login.html est la page pour se connecter , django nous gere la verification et nous redirige vers l'url indiqué dans input type hidden de la page html
    ])),

    #connexion et deconnexion livreur
    path('livreur/', include([
        path('', livreur_views.home),
        path('inscription/', livreur_views.connexionView.as_view()),
        path('thanks/', livreur_views.reponse),
        path('logout/', auth_views.logout,{'template_name':'livreur/home.html',},name='livreur_deconn'),#.logout nous gere la deconnexion , meme pas besoin d'ecrire une methode dans views.py,il nous redirige directement dans le template_name
        path('login/', auth_views.login,{'template_name':'livreur/login.html'}), #meme chose pour .login ,patient/login.html est la page pour se connecter , django nous gere la verification et nous redirige vers l'url indiqué dans input type hidden de la page html
    ])),

]
