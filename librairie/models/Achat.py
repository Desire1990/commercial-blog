from django.db import models
from . import Client, Livre

class Achat(models.Model):
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    livre = models.ForeignKey("Livre", null=True, on_delete=models.SET_NULL)
    somme = models.IntegerField()
    done = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if(self.somme == self.livre.prix):
            self.done=True
        super(Achat, self).save(*args, **kwargs)
