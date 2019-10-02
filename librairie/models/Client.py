from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    tel = models.CharField(max_length=15, verbose_name='numero de téléphone')

    class Meta:
        unique_together=("nom", "prenom","tel")
