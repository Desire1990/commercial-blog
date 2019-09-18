from django.db import models
from django.contrib.auth.models import User

class Personnel(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to="")

class Contact(models.Model):
	name = models.CharField(max_length=64, verbose_name="Full Name")
	tel = models.CharField(max_length=64, verbose_name="Phone Number")
	email = models.EmailField(max_length=64, verbose_name="Email Address")
	message = models.TextField( verbose_name="Message")

	def __str_(self):
		return f"{self.name} : {self.message[:20]}..."