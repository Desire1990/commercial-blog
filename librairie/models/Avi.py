from django.db import models
from . import Livre

class Avi(models.Model):
    user = models.OneToOneField("base.Profil", null=True, on_delete=models.SET_NULL)
    livre = models.ForeignKey("Livre", on_delete=models.CASCADE)
    like = models.BooleanField(null=True)

