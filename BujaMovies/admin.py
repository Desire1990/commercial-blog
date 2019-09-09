from django.contrib import admin
from .models import Avis, Commentaires, Films, Achats

# Register your models here.

admin.site.register( Avis )
admin.site.register( Commentaires )
admin.site.register( Films )
admin.site.register( Achats )
