from django.urls import path,include
from . import views
from patient import views as patient_views
from django.contrib.auth import views as auth_views

"""
from django.contrib.auth import views => classe de django qui nous donne des methode
pour nous permettre de gerer plus facilement la connexion et la deconnexion ...
"""

urlpatterns = [
    path('', views.home), 
    #path pour gerer connexion patient ce sera la meme chose pour les autres apps
    path('patient/', include([
        path('', patient_views.home),
        path('inscription/', patient_views.connexionView.as_view()),
        path('thanks/', patient_views.reponse,name="afficher_reponse"),
        path('logout/', auth_views.logout,{'template_name':'patient/logout.html'}),#.logout nous gere la deconnexion , meme pas besoin d'ecrire une methode dans views.py,il nous redirige directement dans le template_name
        path('login/', auth_views.login,{'template_name':'patient/login.html'}), #meme chose pour .login ,patient/login.html est la page pour se connecter , django nous gere la verification et nous redirige vers l'url indiqué dans input type hidden de la page html
    ])),
]