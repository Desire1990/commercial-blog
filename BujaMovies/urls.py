from django.urls import path
from . import views

urlpatterns = [
 
    path( '', views.acceuil_app, name="movies" ),
    path( 'details_app/<str:slug>', views.details_app, name="details_app" ),
    path('upload_movie/', views.ajout_app, name="upload_movie"),
    # path( 'upload_movie/<str:slug>', views.ajout_app, name="upload_movie" ),

]
