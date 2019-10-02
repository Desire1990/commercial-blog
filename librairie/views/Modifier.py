from django.shortcuts import *
from ..forms import BookForm
from ..models import Livre
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class ModifierView(LoginRequiredMixin, View):
    template_name = "book_form.html"

    def get(self, request, slug):
        page = "UPDATE BOOK"
        url = 'update_book'
        book = Livre.objects.get(slug=slug)
        form = BookForm(instance=book)
        return render(request, "book_form.html", locals())

    def post(self, request, slug):
        book = Livre.objects.get(slug=slug)
        form = BookForm(request.POST, request.FILES, instance=book)
        if request.user.profil == book.owner:
            form.save()
            return redirect("library")
        return render(request, self.template_name, locals())

     