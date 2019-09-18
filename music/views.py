from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *

# Create your views here.
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

    return render(request, 'music/login.html', locals())

def musicList_view(request):
	
	musics = Music.objects.all()

	return render(request, 'music/music-list.html', locals())


def musicDownload_view(request, slug=None):
	music = get_object_or_404(Music.objects.filter(slug = slug))
	return render(request, 'music/download_page.html', locals())

def payement_view(request):
	form = PayementForm(request.POST or None)
	
	if form.is_valid():
		payementMethod = form.cleaned_data['payementMethod']
		montant = form.cleaned_data['montant']
		identifiant = form.cleaned_data['identifiant']

	return render(request, 'music/music_list.html', locals())