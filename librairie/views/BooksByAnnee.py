from django.shortcuts import render
from django.views import View
from ..models import Livre
from django.utils.datastructures import MultiValueDictKeyError
from .book_attr import book_attrs

class BooksByAnneeView(View):
    template_name = "library_content.html"
    model = Livre

    def get(self, request, annee):
        try:
            page = int(request.GET["page"])
        except MultiValueDictKeyError:
            page=1
        books = self.model.objects.filter(annee=annee)
        accueil = False
        nom_app, slide1, slides, pages, page_content = book_attrs(books, page)
        return render(request, self.template_name, locals())
 