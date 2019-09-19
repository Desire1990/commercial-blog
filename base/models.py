from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to="movies/avatars/")
    about = models.TextField(max_length=1000)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Personnel(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to="")

class Contact(models.Model):
	name = models.CharField(max_length=64, verbose_name="Full Name")
	tel = models.CharField(max_length=64, verbose_name="Phone Number")
	email = models.EmailField(max_length=64, verbose_name="Email Address")
	message = models.TextField( verbose_name="Message")

	def __str__(self):
		return f"{self.name} : {self.message[:20]}..."


class Slides(models.Model):
	slide = models.ImageField(upload_to="base/slides/")
	about = models.CharField(max_length=1000)

	def __str__(self):
		return f"{self.about}"
