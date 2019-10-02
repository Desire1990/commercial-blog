from django.shortcuts import *
from django.views import View
from ..models import Livre, Categorie
from django.utils.datastructures import MultiValueDictKeyError
from .book_attr import book_attrs

class BooksByCategorieView(View):
    template_name = "library_content.html"
    model = Livre

    def get(self, request, categorie):
        try:
            page = int(request.GET["page"])
        except MultiValueDictKeyError:
            page=1
        categorie = Categorie.objects.get(categorie=categorie)
        books = self.model.objects.filter(categorie=categorie)
        accueil = False
        nom_app, slide1, slides, pages, page_content = book_attrs(books, page)
        return render(request, self.template_name, locals())
 