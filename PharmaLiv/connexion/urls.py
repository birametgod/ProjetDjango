from django.urls import path,include
from . import views
from patient import views as patient_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home), 
    path('patient/', include([
        path('', patient_views.home),
        path('inscription/', patient_views.connexionView.as_view()),
        path('thanks/', patient_views.reponse,name="afficher_reponse"),
        path('logout/', auth_views.logout,{'template_name':'patient/logout.html'}),
        path('login/', auth_views.login,{'template_name':'patient/login.html'}), 
    ])),
]