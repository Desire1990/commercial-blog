from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.musicList_view, name="music"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('about_music/<slug>/', views.about_music_view, name="about_music"),
    path('music_player/<slug>/', views.music_player_view, name="music_player"),
    path('delete_music/<slug>/', views.delete_music_view, name="delete_music"),
    path('update_music/<id>/', views.update_music_view, name="update_music"),
    path('upload_music/', views.upload, name="upload_music"),
    path('pay/<slug>/', views.payement_view, name="pay"),
    
]