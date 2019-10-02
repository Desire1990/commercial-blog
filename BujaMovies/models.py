from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Film(models.Model):

    user        = models.ForeignKey ( User, on_delete = models.CASCADE )
    titre       = models.CharField ( verbose_name  = "Titre", null=False, max_length = 30, blank = False )
    acteur      = models.CharField ( verbose_name = "Acteur principale", null=False, max_length = 25, blank = False )
    description = models.CharField ( verbose_name = "Description", max_length = 500, null = False, blank = False)
    language    = models.CharField ( verbose_name = "Language", null = True, default = "Eng", max_length = 3 )
    resolution  = models.IntegerField ( verbose_name = "Resolution", blank = False )
    date        = models.DateTimeField ( default = timezone.now )
    slug        = models.SlugField ( unique = True, max_length = 100, null = True )
    cover       = models.ImageField ( upload_to ="movies/Covers/", null = True, blank = True )
    film        = models.FileField ( upload_to ="movies/Videos/", null = True, blank = True  )
    studio      = models.CharField ( verbose_name = "Studio",max_length = 30, blank = False, null = False )
    prix        = models.DecimalField( verbose_name="Prix de Téléchargement", decimal_places = 2,max_digits = 10000, help_text="BIF", null=False, blank=False)
    realisateur = models.CharField(verbose_name="Réalisateur", max_length=50, null=False, blank=True, default="Lui-même")
    likes       = models.ManyToManyField ( User, related_name = 'likes', blank = True )


    def save( self, *args, **kwargs ):
        self.slug = slugify(self.titre[:30]+str(self.date))#to compare if the we found identical values
        super( Film, self ).save( *args, **kwargs )

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.titre}"
        # {self.resolution} {self.acteur} {self.language} {self.description} {self.date}

    def get_absolute_url(self):
        return reverse("details_app", args=[self.id, self.slug])
        
    def all_likes(self):
        return f"{self.likes.count()}"

class Commentaires(models.Model):
    user        = models.ForeignKey ( User, on_delete = models.CASCADE )
    titre       = models.ForeignKey ( Film, verbose_name = "Choisir Titre", on_delete = models.CASCADE )
    commentaire = models.TextField ( verbose_name = "Commenter",null=False, blank = False )
    date        = models.DateTimeField ( default = timezone.now )

    def __str__(self):
        return f"{self.user} made this comment {self.commentaire}"

class Achats(models.Model):
    user        = models.ForeignKey ( User, on_delete = models.CASCADE )
    montant = models.FloatField ( verbose_name = "Montant", blank = False )
    slug    = models.ForeignKey ( Film, on_delete = models.CASCADE, max_length=100, null = False )
    date    = models.DateTimeField ( default = timezone.now )

    def __str__(self):
        return f"{self.user} bought {self.slug} for {self.montant} on {self.date}"
