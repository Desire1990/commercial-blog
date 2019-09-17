from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Films(models.Model):
    required_css_class = 'required'
    user        = models.ForeignKey ( User, on_delete = models.CASCADE )
    titre       = models.CharField ( verbose_name  = "Titre", null=False, max_length = 30, blank = False )
    acteur      = models.CharField ( verbose_name = "Acteur principale", null=False, max_length = 25, blank = False )
    description = models.CharField ( verbose_name = "Description", max_length = 500, null=False, blank = False)
    language    = models.CharField ( verbose_name = "Language", null = True, default = "lang", max_length = 3 )
    resolution  = models.IntegerField ( verbose_name = "Resolution", blank = False )
    date        = models.DateTimeField ( default = timezone.now )
    slug        = models.SlugField (unique=True, max_length=100, null = True )
    cover       = models.ImageField ( upload_to = 'Covers/', null = True )
    film        = models.FileField ( upload_to = 'Videos/', null = True )
    realisateur = models.CharField ( verbose_name = "Réalisateur", max_length = 50, null = False, blank = True, default = "Lui-même")
    studio      = models.CharField ( verbose_name = "Studio",max_length = 30, blank = False, null = False )
    prix_telechargement = models.FloatField ( verbose_name = "Prix de Téléchargement", help_text = "BIF", null = False, blank = False )

    def save(self,*args,**kwargs):
        self.slug = slugify(self.titre[:30]+str(self.date))#to compare if the we found identical values
        super(Films, self).save(*args, **kwargs)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.titre}"
        # {self.resolution} {self.acteur} {self.language} {self.description} {self.date}

class Commentaires(models.Model):
    user        = models.ForeignKey ( User, on_delete = models.CASCADE )
    titre       = models.ForeignKey ( Films, verbose_name = "Choisir Titre", on_delete = models.CASCADE )
    commentaire = models.TextField ( verbose_name = "Commenter",null=False, blank = False )
    date        = models.DateTimeField ( default = timezone.now )

    def __str__(self):
        return f"{self.user} made this comment {self.commentaire}"

class Avis(models.Model):
    user     = models.ForeignKey ( User, on_delete = models.CASCADE )
    slug_key = models.CharField ( max_length=50, verbose_name = "Slug key")
    likes    = models.BooleanField ( default = False )
    dislikes = models.BooleanField ( default = False )

    def __str__(self):
        return f"{self.slug_key} ~ likes: {self.likes} ~dislikes: {self.dislikes}"

class Achats(models.Model):
    user    = models.ForeignKey ( User, on_delete = models.CASCADE )
    montant = models.FloatField ( verbose_name = "Montant", blank = False )
    slug    = models.ForeignKey ( Films, on_delete = models.CASCADE, max_length=100, null = False )
    date    = models.DateTimeField ( default = timezone.now )

    def __str__(self):
        return f"{self.user} bought {self.slug} for {self.montant} on {self.date}"
