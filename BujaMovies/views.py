from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import *
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from base.views import connexion
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
    
def movies_attrs( film_obj, page ):
    try:
        slide1 = film_obj[0]
        slides = film_obj[1:3]
    except IndexError:
        slide1 = None
        slides = None
    pages        = Paginator( film_obj, 2 )
    page_content = pages.page( page )
    pagination   = pages.page_range
    nom_app      = "Movies"
    return (nom_app, slide1, slides, pages, page_content)
    
def acceuil_app( request ):
    nom_app    = "Movies"
    page_title = "Movies" 
    accueil    = True
    film_obj   = Film.objects.all().order_by('date')
    try:
        page = int( request.GET["page"] )
    except MultiValueDictKeyError:
        page = 1
    nom_app, slide1, slides, pages, page_content = movies_attrs( film_obj, page )
    return render( request, 'movies_content.html', locals() )

@login_required  
def like_movie( request ):
    check_thumb = get_object_or_404(Film, id = request.POST.get('film_id'))
    is_liked    = False
    if check_thumb.likes.filter( id = request.user.id ).exists():
        check_thumb.likes.remove( request.user )
        is_liked = False
    else:
        check_thumb.likes.add( request.user )
        is_liked = True
    return HttpResponseRedirect( check_thumb.get_absolute_url() )
    
def details_app( request, id, slug ):
    page_title        = "Movie details" 
    page_content      = Film.objects.get( slug = slug )
    comm_obj          = Commentaires.objects.filter( titre = page_content )
    associated_movies = Film.objects.filter( acteur = page_content.acteur ).order_by('date')
    associated_movies = associated_movies[0:3]

    check_thumb = get_object_or_404( Film, id = id, slug = slug )
    is_liked = False
    
    if check_thumb.likes.filter( id = request.user.id ).exists():
        is_liked = True
    all_likes = check_thumb.all_likes()

    form_view_comm = CommentaireForm( request.POST or None )
    if request.method == "POST":
        if form_view_comm.is_valid():
            current_user = request.user
            com          = form_view_comm.cleaned_data['commentaire']
            Commentaires( user = current_user, titre = page_content, commentaire = com ).save()

    form_view_comm = CommentaireForm()
    return render( request, 'movies_detail.html', locals() )

@login_required
def ajout_app( request ):
    page_title  = "Add movie" 
    all_films   = Film.objects.all().order_by('date')
    form        = FilmForm( request.POST or None, request.FILES )
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

            Film(user = currentuser,titre = titre,acteur = acteur,description = description,language = language,resolution = resolution,cover = cover,film = film,prix = prix,realisateur = realisateur,studio = studio ).save()
            nombre_film = Film.objects.all().count()

        form = FilmForm()
        return redirect( acceuil_app )
    return render(request, 'movies_form.html', locals())
    
@login_required
def update_app( request, id ):
    selected_movie = get_object_or_404( Film, pk = id )
    
    # if not request.user.is_authenticated:
    #     return redirect( connexion )

    if selected_movie.user != request.user:
        return redirect( acceuil_app )

    else:
        page_title = "Update movie" 
        
        if request.method == 'POST':
            form = FilmForm( request.POST or None, request.FILES or None, instance = selected_movie )
            if form.is_valid():
                form.save()
                return redirect( acceuil_app )
                
        else:
            data = {'id'            : selected_movie.id,
                    'user'          : selected_movie.user,
                    'slug'          : selected_movie.slug,
                    'titre'         : selected_movie.titre,
                    'acteur'        : selected_movie.acteur,
                    'description'   : selected_movie.description,
                    'language'      : selected_movie.language,
                    'resolution'    : selected_movie.resolution,
                    'studio'        : selected_movie.studio,
                    'prix'          : selected_movie.prix,
                    'realisateur'   : selected_movie.realisateur,
                    'date'          : selected_movie.date,
                    'cover'         : selected_movie.cover.url,
                    'film'          : selected_movie.film.url,
                    }

            form = FilmForm( initial = data )

    return render( request, 'update_movies_form.html', locals() )

@login_required
def delete_app( request, slug ):
    selected_movie = get_object_or_404( Film, slug = slug )
    get_user       = User.objects.all()
    # if not request.user.is_authenticated:
    #     return redirect( connexion )
    
    if selected_movie.user != request.user:
        return redirect( connexion )

    else:
        page_title     = "Delete movie" 
        if request.method == "POST":
            selected_movie.delete()
            return redirect('../../movies')
        
    return render( request, 'delete_movies.html', locals() )