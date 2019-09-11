from django.urls import path
from . import views

urlpatterns = [
    path('login', views.connexion, name='connexion'),
    path('logout', views.deconnexion, name='deconnexion'),
    path('books', views.books, name='books'), 
    path('book/<slug>', views.book, name='book'), 
]
