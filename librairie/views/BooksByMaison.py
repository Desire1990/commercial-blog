from django.shortcuts import *
from django.views import View
from ..models import Livre
from .book_attr import book_attrs
from django.utils.datastructures import MultiValueDictKeyError

class BooksByMaisonView(View):
    template_name = "library_content.html"
    model = Livre

    def get(self, request, maison):
        try:
            page = int(request.GET["page"])
        except MultiValueDictKeyError:
            page=1
        books = self.model.objects.filter(maison = maison)
        accueil = False
        nom_app, slide1, slides, pages, page_content = book_attrs(books, page)
        return render(request, self.template_name, locals())
 