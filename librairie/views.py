from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout, models
from django.db.models import Q

def connexion(request):
    error = False
    # next = request.GET["next"]
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(accueil)
                # return redirect(next)
            else:
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'login.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))

def accueil(request):
    if request.user.is_authenticated:
        users = models.User.objects.exclude(username=request.user.username)
    else:
        users = models.User.objects.all()
    return render(request, "accueil.html", locals())

def page(request, username, slug=None):
    page_owner = models.User.objects.get(username=username)
    statuts = Statut.objects.filter(Q(user=page_owner)).order_by("-date")
    comments = Commentaire.objects.all()
    if slug!=None : obj_statut = Statut.objects.filter(slug=slug)[0]
    
    if request.method == "POST":
        comment_form = CommentaireForm(request.POST)
        formulaire_message = MessageForm(request.POST)
        if comment_form.is_valid():
            commentaire = comment_form.cleaned_data["commentaire"]
            user = request.user
            try:
                Commentaire(commentaire=commentaire, user=user, statut=obj_statut).save()
            except ValueError:
                Commentaire(commentaire=commentaire, statut=obj_statut).save()

        if formulaire_message.is_valid():
            message = formulaire_message.cleaned_data["contenue"]
            source = request.user
            user = models.User.objects.get(username=username)
            print(message, user, source)
            if user!=source:
                try:
                    Message(user=user, contenue=message, source=source).save()
                except:
                    Message(contenue=message, user=user).save()
            else:
                Statut(user=user, contenue=message).save()
    formulaire_comment = CommentaireForm()
    formulaire_message = MessageForm()
    return render(request, "lire_article.html", locals())