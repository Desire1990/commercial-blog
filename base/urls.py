from django.urls import path
from . import views

urlpatterns = [
    path( 'inscription/', views.inscription, name="inscription" ),
    path( 'connexion/', views.connexion, name="connexion" ),
    path( 'deconnexion/', views.deconnexion, name="deconnexion" ),
    path( '', views.index, name="index" ),
    path( 'contact', views.contact, name="contact" ),
    path( 'about', views.apropos, name="about" ),
]
