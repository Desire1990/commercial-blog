from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import *
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# def movies_attrs( movies, page ):
#     try:
#         slide1 = movies[0]
#         slides = movies[1:3]
#     except IndexError:
#         slide1 = None
#         slides = None
#     pages = Paginator( movies, 10, orphans = 8 )
#     page_content = pages.page( page )
#     pagination = pages.page_range
#     nom_app = "Movies\' Home"
#     return (nom_app, slide1, slides, pages, page_content, pagination)
    


def acceuil_app(request):
    nom_app = "Movies"
    page_title = "Movies" 
    accueil    = True
    film_obj = Film.objects.all().order_by('date')
    slide1=film_obj[0]
    # film_obj=film_obj[1:3]
    page = request.GET.get('page', 1)           # page à charger par defaut
    paginator = Paginator(film_obj, 24)         # limiter tous les elements à afficher

    try:
        filmsPage = paginator.page(page)
    except PageNotAnInteger:
        filmsPage = paginator.page(1)
    except EmptyPage:
        filmsPage = paginator.page(paginator.num_pages)

    return render( request, 'movies_content.html', locals() )

def details_app( request, slug ):
    page_title = "Movie details" 
    page_content = Film.objects.get( slug = slug )
    comm_obj = Commentaires.objects.filter(titre = page_content)
    associated_movies = Film.objects.filter( acteur = page_content.acteur ).order_by('date')
    check_thumbs    = Avis.objects.filter( slug_key = slug )
    associated_movies = associated_movies[0:3]
    all_likes = Avis.objects.filter(Q( likes = True ) & Q( slug_key = slug )).count()
    all_dislikes = Avis.objects.filter(Q( dislikes = True ) & Q( slug_key = slug )).count()

    page = request.GET.get('page', 1)           # page à charger par defaut
    paginator = Paginator(comm_obj, 24)         # limiter tous les elements à afficher

    try:
        filmsPage = paginator.page(page)
    except PageNotAnInteger:
        filmsPage = paginator.page(1)
    except EmptyPage:
        filmsPage = paginator.page(paginator.num_pages)

    # Dealing with the coments form
    form_view_comm = CommentaireForm( request.POST or None )
    if request.method == "POST":
        if form_view_comm.is_valid():
            current_user = request.user
            # titr = form_view_comm.cleaned_data['titre']
            com = form_view_comm.cleaned_data['commentaire']
            Commentaires( user = current_user, titre = page_content, commentaire = com ).save()
            
            all_likes    = Avis.objects.filter(Q( likes = True ) & Q( slug_key = slug ) ).count()
            all_dislikes = Avis.objects.filter(Q( dislikes = True ) & Q( slug_key = slug )).count()
        
    # Dealing with the likes form
    form_view_avi = LikeForm( request.POST or None )

    if request.user.is_authenticated:
        current_user = request.user
        current_email = request.user.email
    else:
        current_user = request.user

    if request.method == "POST":
        if form_view_avi.is_valid():
            like         = form_view_avi.cleaned_data['likes']
            dislike      = form_view_avi.cleaned_data['dislikes']
            Avis( user = current_user,u_email = current_email, slug_key = slug, likes = like, dislikes = dislike ).save()
            all_likes    = Avis.objects.filter(  Q( likes = True ) & Q( slug_key = slug ) ).count()
            all_dislikes = Avis.objects.filter(Q(dislikes=True) & Q(slug_key=slug)).count()
            
    form_view_avi = LikeForm()
    form_view_comm = CommentaireForm()
    return render( request, 'movies_detail.html', locals() )

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
            
            msg = "Saved"
        form = FilmForm()
        return redirect( acceuil_app )
    return render( request, 'movies_form.html', locals() )
    
def update_app(request, id):
    if not request.user.is_authenticated:
        return redirect(movies)
    else:
        page_title      = "Update movie" 
        selected_movie = get_object_or_404(Film, pk = id)
        
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

            form = FilmForm( initial = data)
    

    return render( request, 'update_movies_form.html', locals() )

def delete_app( request, slug ):
    page_title     = "Delete movie" 
    selected_movie = get_object_or_404( Film, slug = slug )
    if request.method == "POST":
        selected_movie.delete()
        return redirect( '../../movies' )
    return render( request, 'delete_movies.html', locals() )




    # selected_movie  = get_object_or_404( Film, slug = slug )

    # data = {'id'            : selected_movie.id,
    #         'user'          : selected_movie.user,
    #         'slug'          : selected_movie.slug,
    #         'titre'         : selected_movie.titre,
    #         'acteur'        : selected_movie.acteur,
    #         'description'   : selected_movie.description,
    #         'language'      : selected_movie.language,
    #         'resolution'    : selected_movie.resolution,
    #         'studio'        : selected_movie.studio,
    #         'prix'          : selected_movie.prix,
    #         'realisateur'   : selected_movie.realisateur,
    #         'date'          : selected_movie.date,
    #         'cover'         : selected_movie.cover.url,
    #         'film'          : selected_movie.film.url,
    #         }
    
    # form = FilmForm( initial = data )
    # if form.is_valid():
    #     form.save()