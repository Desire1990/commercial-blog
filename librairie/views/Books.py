from django.shortcuts import render
from django.views import View
from ..models import Livre
from django.utils.datastructures import MultiValueDictKeyError
from .book_attr import book_attrs

class BooksView(View):
    template_name = "library_content.html"
    model = Livre

    def get(self, request):
        try:
            page = int(request.GET["page"])
        except MultiValueDictKeyError:
            page=1
        books = self.model.objects.all()
        accueil = True
        nom_app, slide1, slides, pages, page_content = book_attrs(books, page)
        return render(request, self.template_name, locals())
