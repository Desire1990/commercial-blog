from django.contrib import admin
from . models import *


class MusicAdmin(admin.ModelAdmin):
	list_display = ('titre', 'auteur', 'anneeSortie', 'date')
	list_filter = ('titre', 'auteur', 'anneeSortie')
	ordering = ('date',)
	search_field = ('titre', 'auteur', 'anneeSortie')

class ProfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')
    list_filter = ('user', 'avatar')
    search_fields = ('user', 'avatar')

admin.site.register(Music, MusicAdmin)
admin.site.register(Profil, ProfilAdmin)