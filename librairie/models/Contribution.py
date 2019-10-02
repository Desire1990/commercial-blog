from django.db import models
from . import Livre

class Contribution(models.Model):
    livre = models.ForeignKey("Livre", on_delete=models.CASCADE)
    contributeur = models.OneToOneField("base.Profil", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.livre} - {self.contributeur}"
