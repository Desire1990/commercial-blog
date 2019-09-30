from django.urls import path
from . import views

urlpatterns = [
 
    path( '', views.acceuil_app, name="movies" ),
    path( 'details_app/<str:slug>', views.details_app, name="details_app" ),
    path( 'upload_movie/', views.ajout_app, name="upload_movie"),
    path( 'update_movie/<int:id>', views.update_app, name="update_movie"),
    path( '<str:slug>/delete_movie', views.delete_app, name="delete_movie" ),

]
