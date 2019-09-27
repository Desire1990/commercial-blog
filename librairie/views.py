from django.shortcuts import *
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, models
from django.db.models import Q
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.utils.datastructures import MultiValueDictKeyError

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

def book_attrs(books, page):
    try:
        slide1 = books[0]
        slides = books[1:3]
    except IndexError:
        slide1 = None
        slides = None
    pages = Paginator(books, 20, orphans=8)
    page_content = pages.page(page)
    nom_app = "Livres"
    return (nom_app, slide1, slides, pages, page_content)

def books(request):
    try:
        page = int(request.GET["page"])
    except MultiValueDictKeyError:
        page=1
    books = Livre.objects.all()
    accueil = True
    nom_app, slide1, slides, pages, page_content = book_attrs(books, page)
    return render(request, "library_content.html", locals())

def books_by_auteur(request, auteur):
    try:
        page = int(request.GET["page"])
    except MultiValueDictKeyError:
        page=1
    auteur = User.objects.get(username=auteur)
    books = Livre.objects.filter(owner=auteur.profil)
    accueil = False
    nom_app, slide1, slides, pages, page_content = book_attrs(books, page)
    return render(request, "library_content.html", locals())
    
def books_by_maison(request, maison):
    try:
        page = int(request.GET["page"])
    except MultiValueDictKeyError:
        page=1
    books = Livre.objects.filter(maison = maison)
    accueil = False
    nom_app, slide1, slides, pages, page_content = book_attrs(books, page)
    return render(request, "library_content.html", locals())
    
def books_by_categorie(request, categorie):
    try:
        page = int(request.GET["page"])
    except MultiValueDictKeyError:
        page=1
    categorie = Categorie.objects.get(categorie=categorie)
    books = Livre.objects.filter(categorie=categorie)
    accueil = False
    nom_app, slide1, slides, pages, page_content = book_attrs(books, page)
    return render(request, "library_content.html", locals())
    
def books_by_annee(request, annee):
    try:
        page = int(request.GET["page"])
    except MultiValueDictKeyError:
        page=1
    books = Livre.objects.filter(annee=annee)
    accueil = False
    nom_app, slide1, slides, pages, page_content = book_attrs(books, page)
    return render(request, "library_content.html", locals())

def book(request, slug):
    book = Livre.objects.get(slug=slug)
    lasts = Livre.objects.filter(owner=book.owner)[:3]
    try:
        like_value = Like.objects.get(what=book,
            who=request.user.profil).like
    except:
        like_value = 0
    return render(request, "library_detail.html", locals())

@login_required(redirect_field_name='login')
def ajouter(request, slug=None):
    page = "ADD BOOK"
    url = 'add_book'
    if request.method=="POST":
        form = BookForm(request.POST, request.FILES)
        book = form.save(commit=False)
        book.owner = request.user.profil
        book.slug = slugify(book.titre)
        book.save()
        print(book.owner, book.slug)
        return redirect("library")
    form = BookForm()
    return render(request, "book_form.html", locals())

def modifier(request, slug):
    page = "UPDATE BOOK"
    url = 'update_book'
    book = Livre.objects.get(slug=slug)
    if request.method=="POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        form.save()
        return redirect("library")
    form = BookForm(instance=book)
    return render(request, "book_form.html", locals())

def supprimer(request, slug):
    book = Livre.objects.get(slug=slug)
    if book.owner.user == request.user:
        book.delete()
    return redirect("library")

@login_required(redirect_field_name='login')
def like(request, slug, new_value):
    book = Livre.objects.get(slug=slug)
    try:
        like = Like.objects.get(what=book, who=request.user.profil)
    except:
        like = Like(what=book, who=request.user.profil)
    if like.like == new_value:
        like.like = 0
    else:
        like.like = new_value
    like.save()
    return redirect("book", slug=slug)
