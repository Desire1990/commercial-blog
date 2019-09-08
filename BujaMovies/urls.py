from django.urls import path
from . import views

urlpatterns = [
    path( '', views.acceuil_view, name="acc" ),
    path( 'profil/<str:slug>', views.profil_view, name="profil" ),
    path( 'inscription/', views.inscription_view, name="inscription" ),
    path( 'connexion/', views.connexion_view, name="connexion" ),
]
