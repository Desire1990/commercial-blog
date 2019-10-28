from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
 
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey('base.profil', on_delete= models.CASCADE,related_name='aauthor')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    image_url = models.CharField(max_length = 255)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    price = models.FloatField()
    stock = models.IntegerField()
    code = models.CharField(max_length = 10)
    categorie = models.ForeignKey('Categorie', on_delete = models.CASCADE)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Categorie(models.Model):
    name = models.CharField(max_length = 30)  

class Comment(models.Model):
    name = models.CharField(max_length = 10)
    email = models.EmailField()
    comment = models.TextField()



