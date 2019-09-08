from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.shortcuts import render
from .forms import FilmForm, CommentaireForm, AvisForm, InscriptionForm, ConnexionForm
from .models import Films, Avis, Commentaires, Achats
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
    
def acceuil_view(request):
    acceuil = "Page d'acceuil"
    film_obj = Films.objects.all()
    nombre_film = Films.objects.all().count()
    form_view_film = FilmForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if form_view_film.is_valid():
            # form_view_film.save()
            currentuser = request.user
            titre = form_view_film.cleaned_data['titre']
            acteur = form_view_film.cleaned_data['acteur']
            description = form_view_film.cleaned_data['description']
            language = form_view_film.cleaned_data['language']
            resolution = form_view_film.cleaned_data['resolution']
            cover = form_view_film.cleaned_data['cover']
            film = form_view_film.cleaned_data['film']
            prix = form_view_film.cleaned_data['prix_telechargement']

            Films(user = currentuser,titre = titre,acteur = acteur,description = description,language = language,resolution = resolution,cover = cover,film = film,prix_telechargement = prix ).save()
            nombre_film = Films.objects.all().count()
            msg = "Enregistrer avec success !!!"
    return render( request, 'acceuil.html',locals() )

def profil_view(request,slug):
    film_obj = Films.objects.get( slug = slug )
    comm_obj = Commentaires.objects.filter( titre = film_obj )
    all_likes = Avis.objects.filter(Q(likes="1")).count()
    all_dislikes = Avis.objects.filter(Q(dislikes="1")).count()
    
    form_view_comm = CommentaireForm(request.POST or None)
    if request.method == "POST":
        if form_view_comm.is_valid():
            current_user = request.user
            # titr = form_view_comm.cleaned_data['titre']
            com = form_view_comm.cleaned_data['commentaire']
            Commentaires(user = current_user,titre = film_obj,commentaire = com).save()
            msg = "Enregistrer avec success !!!"
            form_view_comm = Commentaires()

    form_view_avi = AvisForm(request.POST or None)
    if request.method == "POST":
        if form_view_avi.is_valid():
            current_user = request.user
            film_key = str(current_user)+str(slug)
            Avis( user = current_user, slug_key = film_key, likes = 1 ).save()
            all_likes = Avis.objects.filter(Q(likes="1") & Q(slug_key=film_obj)).count()
            all_dislikes = Avis.objects.filter(Q(dislikes="1") & Q(slug_key=film_obj)).count()
            mssg = "Liked!!!"

    form_view_avi1 = AvisForm(request.POST or None)
    if request.method == "POST":
        if form_view_avi1.is_valid():
            current_user1 = request.user
            film_key1 = str(current_user1)+str(slug)
            Avis( user = current_user1, slug_key = film_key, dislikes = 1 ).save()
            all_likes = Avis.objects.filter(likes="1").count()
            all_dislikes = Avis.objects.filter(dislikes="1").count()
            mssg1 = "Disliked!!!"
 
    return render( request, 'profil.html',locals() )

def inscription_view(request):
    inscription = "S'inscrire"
    form_view_inscr = InscriptionForm(request.POST or None)
    if request.method == "POST":
        if form_view_inscr.is_valid():
            pseudo = form_view_inscr.cleaned_data['pseudo']
            mail = form_view_inscr.cleaned_data['email']
            pass1 = form_view_inscr.cleaned_data['password1']
            pass2 = form_view_inscr.cleaned_data['password2']
            if pass1 == pass2:
                User.objects.create_user(username = pseudo, email = mail, password = pass1)

    return render(request, 'inscription.html', locals() )


def connexion_view(request):
    cone = "Se conncter"
    form_view_con = ConnexionForm(request.POST or None)
    if request.method == "POST":
        if form_view_con.is_valid():
            pseudo = form_view_con.cleaned_data['pseudo']
            pass1 = form_view_con.cleaned_data['password1']
            user = authenticate(username = pseudo, password = pass1)

            if user:
                login(request, user)

    else:
        form = ConnexionForm()

    return render(request, 'connection.html', locals() )




