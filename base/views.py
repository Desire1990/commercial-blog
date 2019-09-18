from django.shortcuts import render
from django.http import HttpResponse
from . models import *

def inscription(request):
	pass

def connexion(request):
	pass

def deconnexion(request):
	pass

def index(request):
	slides = Slides.objects.all()
	slide1 = slides[0]
	slides = slides[1:3]
	return render(request, 'index.html', locals())

def contact(request):
	pass

def apropos(request):
	pass