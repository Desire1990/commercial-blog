from django.urls import path
from . import views

urlpatterns = [
    # path( 'nones', views.acceuil_view, name="acc" ),
    # path( 'profil/<str:slug>', views.profil_view, name="profil" ),
    path( 'inscription/', views.inscription_view, name="inscription" ),
    path( 'connexion/', views.connexion_view, name="connexion" ),
    path( 'deconnexion/', views.deconnexion_view, name="deconnexion" ),

    # nouveaux url

    path( '', views.acceuil_app, name="movies" ),
    path( 'apropos_app/', views.apropos_app, name="apropos_app" ),
    path( 'details_app/<str:slug>', views.details_app, name="details_app" ),
    path( 'contact_app/', views.contact_app, name="contact_app" ),
    path( 'upload_movie/', views.ajout_app, name="upload_movie" ),

]
