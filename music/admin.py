from django.contrib import admin
from . models import *


class MusicAdmin(admin.ModelAdmin):
	list_display = ('titre', 'auteur', 'anneeSortie', 'date')
	list_filter = ('titre', 'auteur', 'anneeSortie')
	ordering = ('date',)
	search_field = ('titre', 'auteur', 'anneeSortie')

admin.site.register(Music, MusicAdmin)