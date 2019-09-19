from django.shortcuts import render

from django.contrib.auth import logout
from django.http import HttpResponse
from BujaMovies.models import Film
from librairie.models import Livre
from music.models import Music
from .forms import *

def inscription(request):
	return HttpResponse("<h1>inscription</h1>")

def connexion(request):
	return HttpResponse("<h1>connexion</h1>")

def deconnexion(request):
	logout(request)
	return HttpResponse("<h1>deconnexion</h1>")

def index(request):
	slide1 = Music.objects.last()
	slide2 = Films.objects.last()
	slide3 = Livre.objects.last()
	return render(request, 'index.html', locals())

def contact(request):
	form = ContactForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			form.save()
	return render(request, "contact.html", locals())

def apropos(request):
	return HttpResponse("<h1>apropos</h1>")