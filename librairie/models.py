from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify

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

class Categorie(models.Model):
    categorie = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.categorie}"

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
    user = models.OneToOneField("base.Profil", null=True, on_delete=models.SET_NULL)
    livre = models.ForeignKey("Livre", on_delete=models.CASCADE)
    like = models.BooleanField(null=True)

class Contribution(models.Model):
    livre = models.ForeignKey("Livre", on_delete=models.CASCADE)
    contributeur = models.OneToOneField("base.Profil", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.livre} - {self.contributeur}"
    
class Livre(models.Model):
    owner = models.ForeignKey("base.Profil", null=True, related_name="auteur", on_delete=models.SET_NULL)
    maison = models.CharField(max_length=30, verbose_name="maison d'edition")
    titre = models.CharField(max_length=30, verbose_name="titre du livre")
    categorie = models.ForeignKey("Categorie", null=True, on_delete=models.SET_NULL)
    cover = models.ImageField(upload_to="librairie/covers")
    description = models.TextField(verbose_name="le contenue du livre")
    annee = models.DateField(default=timezone.now)
    contributeurs = models.ManyToManyField("base.Profil", through='Contribution')
    prix = models.IntegerField(verbose_name="prix")
    livre = models.FileField(upload_to="librairie/livres")    
    version = models.IntegerField(verbose_name="version du livre")
    slug = models.SlugField(unique=True, max_length=30)

    def __str__(self):
        return f"{self.titre} {self.version} {self.annee}"
