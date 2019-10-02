from django.urls import path
from .import views

urlpatterns = [
    # path('logout', views.deconnexion, name='deconnexion'),
    path('books', views.BooksView.as_view(), name='books'), 
    path('books_by_auteur/<auteur>', views.BooksByAuteurView.as_view(), name='bbaut'), 
    path('books_by_maison/<maison>', views.BooksByMaisonView.as_view(), name='bbmais'), 
    path('books_by_categorie/<categorie>', views.BooksByCategorieView.as_view(), name='bbcat'), 
    path('books_by_annee/<annee>', views.BooksByAnneeView.as_view(), name='bban'), 
    path('', views.BooksView.as_view(), name='library'), 
    path('book/<slug>', views.BookView.as_view(), name='book'), 
    path('add_book/', views.AjouterView.as_view(), name='add_book'), 
    path('update_book/<slug>', views.ModifierView.as_view(), name='update_book'), 
    path('remove_book/<slug>', views.SupprimerView.as_view(), name='remove_book'), 
    path('like/<slug>/<new_value>', views.like, name='like'), 
]
