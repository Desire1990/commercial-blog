from django.shortcuts import *
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

def books(request):
    books = Livre.objects.all()
    return render(request, "accueil.html", locals())

def book(request, slug):
    book = Livre.objects.get(slug=slug)
    return HttpResponse(str(book))