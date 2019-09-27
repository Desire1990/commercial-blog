from django.shortcuts import  render, redirect, reverse, get_object_or_404
from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout, models

# Create your views here.

def music_attrs(elements, page):
    try:
        slide1 = elements[0]
        slides = elements[1:3]
    except IndexError:
        slide1 = None
        slides = None
    pages = Paginator(elements, 2, orphans=0)
    page_content = pages.page(page)
    nom_app = "Musiques"
    return (nom_app, slide1, slides, pages, page_content)

def musicList_view(request):
    try:
        page = int(request.GET["page"])
    except MultiValueDictKeyError:
        page=1
    musics = Music.objects.all()
    accueil = True
    nom_app, slide1, slides, pages, page_content = music_attrs(musics, page)
    return render(request, 'music_content.html', locals())

def payement_view(request, slug=None):
    form = PayementForm(request.POST or None)
    if not slug:
        musics = Music.objects.all()
        if form.is_valid():
            payement_method = form.cleaned_data['payement_method']
            amount = form.cleaned_data['amount']
            identification = form.cleaned_data['identification']
    else:
        musics = Music.objects.filter(slug=slug)

    return render(request, 'pay_download.html', locals())

def music_player_view(request, slug=None):
    if not slug:
        musics = Music.objects.all()
    else:
        musics = Music.objects.filter(slug=slug)

    return render(request, 'music_player.html', locals())


def about_music_view(request, slug=None):
    if not slug:
    	musics = Music.objects.all()
    else:
        musics = Music.objects.filter(slug=slug)

    return render(request, 'music_detail.html', locals())


def login_view(request):
    error = False
    # next = request.GET["next"]
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(musicList_view)
            else:
                error = True
    else:
        form = LoginForm()

    return render(request, 'login.html', locals())

def logout_view(request):
    logout(request)
    return redirect(reverse(musicList_view))

def upload(request):
    form = MusicForm(request.POST or None)
    return render(request, 'upload_music.html', locals())

def register(request):
    if request.method == 'POST':
        form = UserCreationForm()

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('music')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'register.html', context)