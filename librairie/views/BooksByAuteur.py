from django.shortcuts import *
from ..models import Livre
from django.views import View
from .book_attr import book_attrs
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError


class BooksByAuteurView(View):
    template_name = "library_content.html"
    model = Livre

    def get(self, request, auteur):
        try:
            page = int(request.GET["page"])
        except MultiValueDictKeyError:
            page=1
        auteur = User.objects.get(username=auteur)
        books = self.model.objects.filter(owner=auteur.profil)
        accueil = False
        nom_app, slide1, slides, pages, page_content = book_attrs(books, page)
        return render(request, self.template_name, locals())
 