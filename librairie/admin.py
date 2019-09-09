from django.contrib import admin
from .models import *

class CommentAdmin(admin.ModelAdmin):
    list_display = ('livre', 'commentaire', 'date', 'user', 'visible')
    list_filter = ('livre', 'commentaire', 'date', 'user', 'visible')
    search_fields = ('livre', 'commentaire', 'date', 'user', 'visible')

class LivreAdmin(admin.ModelAdmin):
    list_display = ('auteur', 'maison', 'titre', 'categorie', 'cover', 'contenue', 'annee', 'prix', 'version')
    list_filter = list_display
    search_fields = list_display
    prepopulated_fields = {'slug': ('titre', )}

class AviAdmin(admin.ModelAdmin):
    list_display = ('livre', 'user', 'like')
    list_filter = ('livre', 'user', 'like')
    search_fields = ('livre', 'user', 'like')

class ProfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')
    list_filter = ('user', 'avatar')
    search_fields = ('user', 'avatar')
    
class ClientAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", 'tel')
    list_filter = ("nom", "prenom", 'tel')
    search_fields = ("nom", "prenom", 'tel')
    
class AchatAdmin(admin.ModelAdmin):
    list_display = ("client", "livre", "somme", 'done')
    list_filter = ("client", "livre", "somme", 'done')
    search_fields = ("client", "livre", "somme", 'done')

admin.site.register(Commentaire, CommentAdmin)
admin.site.register(Livre, LivreAdmin)
admin.site.register(Avi, AviAdmin)
admin.site.register(Profil, ProfilAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Achat, AchatAdmin)
admin.site.register(Categorie)