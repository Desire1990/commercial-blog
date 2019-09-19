from django.contrib import admin
from . models import *

class MusicAdmin(admin.ModelAdmin):
	list_display = ('titre', 'owner', 'release', 'date', 'price')
	list_filter = ('titre', 'owner', 'release')
	ordering = ('date',)
	search_field = ('titre', 'owner', 'release')

class PayementAdmin(admin.ModelAdmin):
    list_display = ('payement_method', 'amount', 'identification')
    list_filter = ('payement_method', 'amount', 'identification')
    search_fields = ('payement_method', 'amount', 'identification')

class PayementMethodAdmin(admin.ModelAdmin):
    list_display = ('ecocash', 'lumicash')
    list_filter = ('ecocash', 'lumicash')
    search_fields = ('ecocash', 'lumicash')

admin.site.register(Music, MusicAdmin)
admin.site.register(Payement, PayementAdmin)
admin.site.register(PayementMethod, PayementMethodAdmin)