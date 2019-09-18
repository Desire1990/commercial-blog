from django.contrib import admin
from . models import *


class SlidesAdmin(admin.ModelAdmin):
    list_display = ('slides',)
    list_filter = ('slides',)
    ordering = ('slides',)
    search_field = ('slides',)

class MusicAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'release', 'date', 'price')
	list_filter = ('title', 'author', 'release')
	ordering = ('date',)
	search_field = ('title', 'author', 'release')

class ProfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')
    list_filter = ('user', 'avatar')
    search_fields = ('user', 'avatar')

class PayementAdmin(admin.ModelAdmin):
    list_display = ('payement_method', 'amount', 'identification')
    list_filter = ('payement_method', 'amount', 'identification')
    search_fields = ('payement_method', 'amount', 'identification')

class PayementMethodAdmin(admin.ModelAdmin):
    list_display = ('ecocash', 'lumicash')
    list_filter = ('ecocash', 'lumicash')
    search_fields = ('ecocash', 'lumicash')

class ComposerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name')
    list_filter = ('name', 'last_name')
    search_fields = ('name', 'last_name')

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'about', 'birthday')
    list_filter = ('name', 'last_name', 'about', 'birthday')
    search_fields = ('name', 'last_name', 'about', 'birthday')

class LabelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name', )
    search_fields = ('name',)


admin.site.register(Music, MusicAdmin)
admin.site.register(Profil, ProfilAdmin)
admin.site.register(Payement, PayementAdmin)
admin.site.register(PayementMethod, PayementMethodAdmin)
admin.site.register(Composer, ComposerAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Slides, SlidesAdmin)