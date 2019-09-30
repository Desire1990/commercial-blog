from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from BujaMovies.models import Film
from librairie.models import Livre
from music.models import Music
from .forms import *

def inscription(request):
	if request.method == "POST" :
		form = InscriptionForm(request.POST, request.FILES)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			password2 = form.cleaned_data['password2']
			email = form.cleaned_data['email']
			avatar = form.cleaned_data['avatar']
			if password==password2:
				user = User.objects.create_user(
					username=username, 
					email=email, 
					password=password)
				Profil(user=user, avatar=avatar).save()
		if user:
			login(request, user)
			return redirect(index)
	form = InscriptionForm()
	return render(request, 'inscription.html', locals())

def connexion(request):
	formulaire = ConnexionForm(request.POST)
	if request.method == "POST" and formulaire.is_valid():
		username = formulaire.cleaned_data['username']
		password = formulaire.cleaned_data['password']
		print(username, password)
		user = authenticate(username = username, password = password)
		if user:  # Si l'objet renvoyé n'est pas None
			login(request, user)
			return redirect(index)
	formulaire = ConnexionForm()
	return render(request, 'sign-in.html', locals())



def deconnexion(request):
	logout(request)
	return redirect(index)

def index(request):
	musics = Music.objects.all()
	musics = musics[0:3]
	slide1 = Music.objects.last()
	slide2 = Film.objects.last()
	slide3 = Livre.objects.last()
	return render(request, 'index.html', locals())

def contact(request):
	form = ContactForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			form.save()
	form = ContactForm()
	return render(request, "contact.html", locals())

def apropos(request):
	return render(request, "about.html", locals())