from django.db import models

class Categorie(models.Model):
    categorie = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.categorie}"
