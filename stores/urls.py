from . import views
from django.urls import path


urlpatterns = [
    path('', views.accueil, name = 'stores'),
    path('view/<int:pk>', views.post_view, name='post_view'),
    path('new', views.post_create, name='post_new'),
    path('edit/<int:pk>', views.post_update, name='post_edit'),
    path('delete/<int:pk>', views.post_delete, name='post_delete'),
]
