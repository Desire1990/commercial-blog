from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.shortcuts import redirect

class Composition(models.Model):
    music = models.ForeignKey('Music', on_delete=models.CASCADE)
    composer = models.OneToOneField("base.Profil", on_delete=models.CASCADE)

    def __str__(self):
        return "{0} vendu par {1}".format(self.produit, self.vendeur)

class Music(models.Model):
	audio = models.FileField(upload_to="music/audios/")
	ringtone = models.FileField(upload_to="music/audios/ringtone/", null=True)
	cover = models.ImageField(upload_to="music/covers/")
	titre = models.TextField(max_length=1000)
	owner = models.ForeignKey("base.Profil", null=True, related_name='owner', on_delete=models.SET_NULL)
	composers = models.ManyToManyField("base.Profil", null=True, through='Composition')
	description = models.TextField(verbose_name="a propos de la musique")
	slug = models.SlugField(max_length=1000)
	price = models.IntegerField()
	release = models.DateTimeField(verbose_name='Année de sortie', null=True)
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f"{self.owner} : {self.titre} le {self.date}"

	def save(self, *args, **kwargs):
		self.slug = slugify(self.titre)+str(self.date)
		super(Music, self).save(*args, **kwargs)


class PayementMethod(models.Model):
	lumicash = models.TextField(max_length=100)
	ecocash = models.TextField(max_length=100)

	def __str__(self):
		return f"{self.lumicash} {self.ecocash}"


class Payement(models.Model):
	payement_method = models.OneToOneField("PayementMethod", null=True, on_delete=models.SET_NULL)
	amount = models.IntegerField()
	identification = models.IntegerField()

	def __str__(self):
		return self.payement_method


