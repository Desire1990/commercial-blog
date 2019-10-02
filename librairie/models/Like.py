from django.db import models

class Like(models.Model):
    who = models.ForeignKey("base.Profil", null=True, on_delete=models.SET_NULL)
    what = models.ForeignKey("Livre", on_delete=models.CASCADE)
    like = models.ImageField(max_length=1, default=0)

    class Meta:
        unique_together = ("who","what")
    
    def __str__(self):
        return f"{self.who} => {self.what} : {self.like}"
