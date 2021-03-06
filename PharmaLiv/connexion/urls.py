from django.urls import path,include
from . import views
from payementLigne import views as panier_views
from patient import views as patient_views
from pharmacie import views as pharmacie_views
from medecin import views as medecin_views
from livreur import views as livreur_views
from userAdmin import views as userAdmin_views
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
        path('thanks/', patient_views.reponse,name="afficher_repons"),
        path('logout/', auth_views.logout,{'template_name':'connexion/home.html'},name='patient_deconn'),#.logout nous gere la deconnexion , meme pas besoin d'ecrire une methode dans views.py,il nous redirige directement dans le template_name
        path('login/', auth_views.login,{'template_name':'patient/login.html'}), #meme chose pour .login ,patient/login.html est la page pour se connecter , django nous gere la verification et nous redirige vers l'url indiqué dans input type hidden de la page html
    ])),

    #connexion et deconnexion pharmacie
    path('pharmacie/', include([
        path('', pharmacie_views.home),
        path('inscription/', pharmacie_views.connexionView.as_view()),
        path('thanks/', pharmacie_views.reponse.as_view(),name="afficher_reponse"),
        path('logout/', auth_views.logout,{'template_name':'connexion/home.html'},name='pharmacie_deconn'),#.logout nous gere la deconnexion , meme pas besoin d'ecrire une methode dans views.py,il nous redirige directement dans le template_name
        path('login/', auth_views.login,{'template_name':'pharmacie/login.html'}), #meme chose pour .login ,patient/login.html est la page pour se connecter , django nous gere la verification et nous redirige vers l'url indiqué dans input type hidden de la page html
	    path('partenaire/', pharmacie_views.partenaire), 
	    path('partenaire/<int:id>', pharmacie_views.partenaire,name="afficher_medoc"),
        path('detail/<int:id>',pharmacie_views.detail,name="show_medoc"),
	    path('nonpartenaire/', pharmacie_views.nonpartenaire),
        path('commande', pharmacie_views.creer_commande,name="creer_commande"),
        path('cree/', pharmacie_views.compte),
        path('produi/<int:id>', pharmacie_views.comm_prod,name="comm_produit"),
        path('livreur/<int:id>', pharmacie_views.livre_produit,name="indilma_produit"), 
        path('search/', pharmacie_views.search),
    ])),

    #connexion et deconnexion medecin
    path('medecin/', include([
        path('', medecin_views.home),
        path('inscription/', medecin_views.connexionView.as_view()),
        path('thanks/', medecin_views.reponse.as_view(),name="afficher_reponse"),
        path('logout/', auth_views.logout,{'template_name':'connexion/home.html',},name='medecin_deconn'),#.logout nous gere la deconnexion , meme pas besoin d'ecrire une methode dans views.py,il nous redirige directement dans le template_name
        path('login/', auth_views.login,{'template_name':'medecin/login.html'}), #meme chose pour .login ,patient/login.html est la page pour se connecter , django nous gere la verification et nous redirige vers l'url indiqué dans input type hidden de la page html
    ])),

    #connexion et deconnexion livreur
    path('livreur/', include([
        path('', livreur_views.home),
        path('inscription/', livreur_views.connexionView.as_view()),
        path('notifications/<int:id>', livreur_views.MisAjourNotif, name="notifier"),
        path('livree/<int:id>/<int:idp>', livreur_views.MisAjourCmd, name="livree"),
        path('thanks/', livreur_views.SampleFormView.as_view()),
        path('logout/', auth_views.logout,{'template_name':'livreur/home.html',},name='livreur_deconn'),#.logout nous gere la deconnexion , meme pas besoin d'ecrire une methode dans views.py,il nous redirige directement dans le template_name
        path('login/', auth_views.login,{'template_name':'livreur/login.html'}), #meme chose pour .login ,patient/login.html est la page pour se connecter , django nous gere la verification et nous redirige vers l'url indiqué dans input type hidden de la page html
    ])),

    path('userAdmin/', include([
        path('', auth_views.login,{'template_name':'userAdmin/login.html'}),
        path('inscription/', userAdmin_views.connexionView.as_view(), name="adminInsc"),
        path('zone/', userAdmin_views.zone, name='zone_form'),
        path('thanks/', userAdmin_views.home),
        path('logout/', auth_views.logout,{'template_name':'userAdmin/home.html',},name='userAdmin_deconn'),#.logout nous gere la deconnexion , meme pas besoin d'ecrire une methode dans views.py,il nous redirige directement dans le template_name
        path('login/', auth_views.login,{'template_name':'userAdmin/login.html'}), #meme chose pour .login ,patient/login.html est la page pour se connecter , django nous gere la verification et nous redirige vers l'url indiqué dans input type hidden de la page html
    ])),
    
    path('panier/', include([
        path('', panier_views.panier_detail,name="panier_detail"),
        path('add/<int:id>', panier_views.add_panier, name='add_panier'),

        ])),
        
    path('panier/', include([
        path('', panier_views.panier_detail,name="panier_detail"),
        path('add/<int:id>', panier_views.add_panier, name='add_panier'),
        path('sup/<int:id>', panier_views.supprimer_panier, name='sup_panier'),
    ])),

]

