from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponse
from .models import *
from .forms import *

def inscription(request):
	return HttpResponse("<h1>inscription</h1>")

def connexion(request):
	return HttpResponse("<h1>connexion</h1>")

def deconnexion(request):
	logout(request)
	return HttpResponse("<h1>deconnexion</h1>")

def index(request):
	return HttpResponse("<h1>index</h1>")

def contact(request):
	form = ContactForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			form.save()
	return render(request, "contact.html", locals())

def apropos(request):
	return HttpResponse("<h1>apropos</h1>")