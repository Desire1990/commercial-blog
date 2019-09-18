from django.contrib import admin
from . models import *

class SlidesAdmin(admin.ModelAdmin):
    list_display = ('slide','about',)
    list_filter = ('slide','about',)
    ordering = ('slide', 'about',)
    search_field = ('slide', 'about',)


admin.site.register(Slides, SlidesAdmin)

# Register your models here.

admin.site.register( Contact )
admin.site.register( Personnel )
