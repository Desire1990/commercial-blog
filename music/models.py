from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


class Profil(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL, related_name="Customer")
    avatar = models.ImageField(null=True, blank=True, upload_to="music/avatars/")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Slides(models.Model):
	slides = models.ImageField(null=True, blank=True, upload_to="music/slides/")
	


class Artist(models.Model):
	name = models.TextField(max_length=1000)
	last_name = models.TextField(max_length=1000)
	about = models.TextField(max_length=1000)
	birthday = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f"{self.name} {self.last_name}"

class Composer(models.Model):
	name = models.TextField(max_length=1000)
	last_name = models.TextField(max_length=1000)
	def __str__(self):
		return f"{self.name} {self.last_name}"

class Label(models.Model):
	name = models.TextField(max_length=1000)
	def __str__(self):
		return f"{self.name}"
	


class Music(models.Model):
	audio = models.FileField(upload_to="music/audios/")
	ringtone = models.FileField(upload_to="music/audios/ringtone/", null=False)
	cover = models.ImageField(upload_to="music/covers/")
	title = models.TextField(max_length=1000)
	author = models.ForeignKey("Artist", null=True, on_delete=models.SET_NULL)
	composer = models.ForeignKey("Composer", null=True, on_delete=models.SET_NULL)
	label = models.ForeignKey("Label", null=True, on_delete=models.SET_NULL)
	slug = models.SlugField(max_length=1000)
	price = models.IntegerField()
	release = models.DateTimeField(verbose_name='Année de sortie')
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f"{self.author} : {self.title} le {self.date}"

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)+str(self.date)
		super(Music, self).save(*args, **kwargs)


class PayementMethod(models.Model):
	lumicash = models.TextField(max_length=100)
	ecocash = models.TextField(max_length=100)

	def __str__(self):
		return f"{self.lumicash} {self.ecocash}"


class Payement(models.Model):
	payement_method = models.ForeignKey("PayementMethod", null=True, on_delete=models.SET_NULL)
	amount = models.IntegerField()
	identification = models.IntegerField()

	def __str__(self):
		return self.payement_method
