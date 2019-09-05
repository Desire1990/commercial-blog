from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify

class Profil(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    avatar = models.ImageField(null=True, blank=True, upload_to="media/")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Commentaire(models.Model):
    livre = models.ForeignKey('Livre', on_delete=models.CASCADE)
    commentaire = models.TextField()
    date = models.DateTimeField(verbose_name="Date de parution", default=timezone.now)
    visible = models.BooleanField(default=True)
    user = models.ForeignKey("Profil", verbose_name="auteur du commentaire", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.commentaire}"
    class Meta:
        verbose_name = "avis des lecteurs"

class Categorie(models.Model):
    categorie = models.CharField(max_length=30)

class Client(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    tel = models.CharField(max_length=15, verbose_name='numero de téléphone')

    class Meta:
        unique_together=("nom", "prenom","tel")

class Achat(models.Model):
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    livre = models.ForeignKey("Livre", null=True, on_delete=models.SET_NULL)
    somme = models.IntegerField()
    done = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if(self.somme == self.livre.prix):
            self.done=True
        super(Achat, self).save(*args, **kwargs)

class Avi(models.Model):
    user = models.ForeignKey("Profil", null=True, on_delete=models.SET_NULL)
    livre = models.ForeignKey("Livre", on_delete=models.CASCADE)
    like = models.BooleanField(null=True)
    
class Livre(models.Model):
    auteur = models.CharField(max_length=30, verbose_name="auteur du livre")
    maison = models.CharField(max_length=30, verbose_name="maison d'edition")
    titre = models.CharField(max_length=30, verbose_name="titre du livre")
    categorie = models.ForeignKey("Categorie", null=True, on_delete=models.SET_NULL)
    cover = models.ImageField(upload_to="covers/")
    contenue = models.TextField(verbose_name="le contenue du livre")
    annee = models.DateField(default=timezone.now)
    prix = models.IntegerField(verbose_name="prix")
    version = models.IntegerField(verbose_name="auteur du livre")
    slug = models.SlugField(unique=True, max_length=30)

    def __str__(self):
        return f"{self.titre} {self.version} {self.annee}"