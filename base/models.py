from django.db import models
from django.contrib.auth import User

class Personnel(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to="")

class Contact(models.Model):
	name = models.CharField(verbose_name="Full Name")
	tel = models.CharField(verbose_name="Phone Number")
	email = models.EmailField(verbose_name="Email Address")
	message = models.TextField( verbose_name="Message")

	def __str_(self):
		return f"{self.name} : {self.message[:20]}..."