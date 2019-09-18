from django.urls import path
from . import views

urlpatterns = [
    path('login', views.connexion, name='connexion'),
    path('logout', views.deconnexion, name='deconnexion'),
    path('books/<page>', views.books, name='books'), 
    path('books_by_auteur/<auteur>/<page>', views.books_by_auteur, name='bbaut'), 
    path('books_by_maison/<maison>/<page>', views.books_by_maison, name='bbmais'), 
    path('books_by_categorie/<categorie>/<page>', views.books_by_categorie, name='bbcat'), 
    path('books_by_annee/<annee>/<page>', views.books_by_annee, name='bban'), 
    path('', views.books, name='library'), 
    path('book/<slug>', views.book, name='book'), 
    path('add_book', views.ajouter, name='add_book'), 
    path('update_book/<slug>', views.modifier, name='update_book'), 
    path('remove_book/<slug>', views.supprimer, name='remove_book'), 
]
