from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.showUser),
    path('thanks/', views.reponse,name="afficher_reponse"),
    path('logout/', auth_views.logout,{'template_name':'patient/logout.html'}),
    path('login/', auth_views.login,{'template_name':'patient/login.html'}), 
]