from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


class Music(models.Model):
	audio = models.FileField(upload_to="audios/")
	cover = models.ImageField(upload_to="covers/")
	titre = models.TextField(max_length=1000)
	auteur = models.TextField(max_length=1000)
	slug = models.SlugField(max_length=1000)
	anneeSortie = models.DateTimeField(verbose_name='Année de sortie')
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f"{self.auteur} : {self.titre} le {self.date}"

	def save(self, *args, **kwargs):
		self.slug = slugify(self.titre[:5])
		super(Music, self).save(*args, **kwargs)


class PayementMethod(models.Model):
	lumicash = models.IntegerField()
	ecocash = models.IntegerField()

	def __str__(self):
		return self.lumicash + ' ' + self.ecocash


class Payement(models.Model):
	payementMethod = models.ForeignKey(PayementMethod, on_delete = models.CASCADE)
	montant = models.IntegerField()
	identifiant = models.IntegerField()
	


	def __str__(self):
		return self.identifiant
