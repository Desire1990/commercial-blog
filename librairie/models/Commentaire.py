from django.db import models
from django.utils import timezone

class Commentaire(models.Model):
    livre = models.ForeignKey('Livre', on_delete=models.CASCADE)
    commentaire = models.TextField()
    date = models.DateTimeField(verbose_name="Date de parution", default=timezone.now)
    visible = models.BooleanField(default=True)
    user = models.ForeignKey("base.Profil", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.commentaire}"
    class Meta:
        verbose_name = "avis des lecteurs"
