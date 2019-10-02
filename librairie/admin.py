from django.contrib import admin
from .models import *

class CommentAdmin(admin.ModelAdmin):
    list_display = ('livre', 'commentaire', 'date', 'user', 'visible')
    list_filter = ('livre', 'commentaire', 'date', 'user', 'visible')
    search_fields = ('livre', 'commentaire', 'date', 'user', 'visible')

class LivreAdmin(admin.ModelAdmin):
    list_display = ('owner', 'maison', 'titre', 'categorie', 'cover', 'annee', 'prix', 'version')
    list_filter = ('owner', 'maison', 'titre', 'categorie', 'cover', 'annee', 'prix', 'version')
    search_fields = ('owner', 'maison', 'titre', 'categorie', 'cover', 'annee', 'prix', 'version')
    prepopulated_fields = {'slug': ('titre', )}

class AviAdmin(admin.ModelAdmin):
    list_display = ('livre', 'user', 'like')
    list_filter = ('livre', 'user', 'like')
    search_fields = ('livre', 'user', 'like')
    
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
admin.site.register(Client, ClientAdmin)
admin.site.register(Achat, AchatAdmin)
admin.site.register(Categorie)
admin.site.register(Contribution)
admin.site.register(Like)
