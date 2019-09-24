from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def movies_attrs(movies, page):
    try:
        slide1 = movies[0]
        slides = movies[1:3]
    except IndexError:
        slide1 = None
        slides = None
    pages = Paginator(movies, 20, orphans=8)
    page_content = pages.page(page)
    pagination = pages.page_range
    nom_app = "Films"
    return (nom_app, slide1, slides, pages, page_content, pagination)

def acceuil_app(request):
    accueil = True
    movies = Film.objects.all().order_by('date')
    nom_app, slide1, slides, pages, page_content, pagination = movies_attrs(movies, 1)
    return render(request, 'movies_content.html', locals() )

def details_app(request,slug):
    page_content = Film.objects.get(slug = slug)
    comm_obj = Commentaires.objects.filter( titre = page_content )
    associated_movies = Film.objects.filter(acteur = page_content.acteur).order_by('date')
    check_thumbs    = Avis.objects.filter( slug_key = slug )
    associated_movies = associated_movies[0:3]
    all_likes = Avis.objects.filter(Q(likes=True) & Q(slug_key=slug)).count()
    all_dislikes = Avis.objects.filter(Q(dislikes=True) & Q(slug_key=slug)).count()

    form_view_comm = CommentaireForm(request.POST or None)
    if request.method == "POST":
        if form_view_comm.is_valid():
            current_user = request.user
            # titr = form_view_comm.cleaned_data['titre']
            com = form_view_comm.cleaned_data['commentaire']
            Commentaires( user = current_user, titre = page_content, commentaire = com ).save()
            msg = "Enregistrer avec success !!!"
            form_view_comm = Commentaires()
            all_likes    = Avis.objects.filter(Q(likes=True) & Q(slug_key=slug) ).count()
            all_dislikes = Avis.objects.filter(Q(dislikes=True) & Q(slug_key=slug)).count()

    form_view_avi = LikeForm(request.POST or None)

    current_user    = request.user
    current_email   = request.user.email
    for thumbs in check_thumbs:
        print("")

    if request.method == "POST":
        if form_view_avi.is_valid():
            like         = form_view_avi.cleaned_data['likes']
            dislike      = form_view_avi.cleaned_data['dislikes']
            Avis( user = current_user,u_email = current_email, slug_key = slug, likes = like, dislikes = dislike ).save()
            all_likes    = Avis.objects.filter(Q(likes=True) & Q(slug_key=slug) ).count()
            all_dislikes = Avis.objects.filter(Q(dislikes=True) & Q(slug_key=slug)).count()

    return render(request, 'movies_detail.html', locals() )

def ajout_app(request):
    all_films = Film.objects.all().order_by('date')
    form = FilmForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            # form_view_film.save()
            currentuser      = request.user
            titre            = form.cleaned_data['titre']
            acteur           = form.cleaned_data['acteur']
            description      = form.cleaned_data['description']
            language         = form.cleaned_data['language']
            resolution       = form.cleaned_data['resolution']
            cover            = form.cleaned_data['cover']
            film             = form.cleaned_data['film']
            prix             = form.cleaned_data['prix']
            studio           = form.cleaned_data['studio']
            realisateur      = form.cleaned_data['realisateur']

            # Film(user = currentuser,titre = titre,acteur = acteur,description = description,language = language,resolution = resolution,cover = cover,film = film,prix = prix,realisateur = realisateur,studio = studio ).save()
            # nombre_film = Film.objects.all().count()
            
            # msg = "Enregistrer avec success !!!"
    return render(request, 'movies_form.html', locals() )
