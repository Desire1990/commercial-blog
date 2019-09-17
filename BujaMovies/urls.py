from django.urls import path
from . import views

urlpatterns = [
    # path( 'nones', views.acceuil_view, name="acc" ),
    # path( 'profil/<str:slug>', views.profil_view, name="profil" ),
    path( 'inscription/', views.inscription_view, name="inscription" ),
    path( 'connexion/', views.connexion_view, name="connexion" ),

    # nouveaux url

    path( '', views.acceuil_app, name="acceuil_app" ),
    path( 'apropos_app/', views.apropos_app, name="apropos_app" ),
    path( 'details_app/<str:slug>', views.details_app, name="details_app" ),
    path( 'contact_app/', views.contact_app, name="contact_app" ),
    path( 'ajout_app/', views.ajout_app, name="ajout_app" ),
]
