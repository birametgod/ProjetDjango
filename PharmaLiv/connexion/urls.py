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
        path('', patient_views.home),
        path('inscription/', patient_views.connexionView.as_view()),
        path('thanks/', patient_views.reponse,name="afficher_reponse"),
        path('logout/', auth_views.logout,{'template_name':'patient/logout.html'},name='patient_deconn'),#.logout nous gere la deconnexion , meme pas besoin d'ecrire une methode dans views.py,il nous redirige directement dans le template_name
        path('login/', auth_views.login,{'template_name':'patient/login.html'}), #meme chose pour .login ,patient/login.html est la page pour se connecter , django nous gere la verification et nous redirige vers l'url indiqué dans input type hidden de la page html
    ])),

    #connexion et deconnexion pharmacie
    path('pharmacie/', include([
        path('', pharmacie_views.home),
        path('inscription/', pharmacie_views.connexionView.as_view()),
        path('thanks/', pharmacie_views.reponse,name="afficher_reponse"),
        path('logout/', auth_views.logout,{'template_name':'pharmacie/logout.html'}),#.logout nous gere la deconnexion , meme pas besoin d'ecrire une methode dans views.py,il nous redirige directement dans le template_name
        path('login/', auth_views.login,{'template_name':'pharmacie/login.html'}), #meme chose pour .login ,patient/login.html est la page pour se connecter , django nous gere la verification et nous redirige vers l'url indiqué dans input type hidden de la page html
    ])),

    #connexion et deconnexion medecin
    path('medecin/', include([
        path('', medecin_views.home),
        path('inscription/', medecin_views.connexionView.as_view()),
        path('thanks/', medecin_views.reponse,name="afficher_reponse"),
        path('logout/', auth_views.logout,{'template_name':'medecin/logout.html',},name='medecin_deconn'),#.logout nous gere la deconnexion , meme pas besoin d'ecrire une methode dans views.py,il nous redirige directement dans le template_name
        path('login/', auth_views.login,{'template_name':'medecin/login.html'}), #meme chose pour .login ,patient/login.html est la page pour se connecter , django nous gere la verification et nous redirige vers l'url indiqué dans input type hidden de la page html
    ])),

]
