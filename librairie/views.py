from django.shortcuts import *
from .forms import *
from .models import *
from django.core.paginator import Paginator
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

def book_attrs(books, page):
    slide1 = books[0]
    slides = books[1:3]
    pages = Paginator(books, 20, orphans=8)
    page_content = pages.page(page)
    pagination = pages.page_range
    return (slide1, slides, pages, page_content, pagination)

def books(request, page=1):
    books = Livre.objects.all()
    accueil = True
    slide1, slides, pages, page_content, pagination = book_attrs(books, page)
    return render(request, "library/accueil.html", locals())

def books_by_auteur(request, auteur, page):
    books = Livre.objects.filter(id=auteur)
    accueil = False
    slide1, slides, pages, page_content, pagination = book_attrs(books, page)
    return render(request, "library/accueil.html", locals())
    
def books_by_maison(request, maison, page):
    books = Livre.objects.filter(maison = maison)
    accueil = False
    slide1, slides, pages, page_content, pagination = book_attrs(books, page)
    return render(request, "library/accueil.html", locals())
    
def books_by_categorie(request, categorie, page):
    categorie = Categorie.objects.get(categorie=categorie)
    books = Livre.objects.filter(categorie=categorie)
    accueil = False
    slide1, slides, pages, page_content, pagination = book_attrs(books, page)
    return render(request, "library/accueil.html", locals())
    
def books_by_annee(request, annee, page):
    books = Livre.objects.filter(annee=annee)
    accueil = False
    slide1, slides, pages, page_content, pagination = book_attrs(books, page)
    return render(request, "library/accueil.html", locals())

def book(request, slug):
    book = Livre.objects.get(slug=slug)
    lasts = Livre.objects.filter(auteur=book.auteur)[:3]
    return render(request, "library/detail.html", locals())

def ajouter(request, slug):
    pass
def modifier(request, slug):
    pass
def supprimer(request, slug):
    pass