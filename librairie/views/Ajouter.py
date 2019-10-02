from django.shortcuts import render, redirect
from ..forms import BookForm
from django.utils.text import slugify
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class AjouterView(LoginRequiredMixin, View):
    template_name = "book_form.html"

    def get(self, request):
        page = "ADD BOOK"
        form = BookForm()
        return render(request, self.template_name, locals())

    def post(self, request):
        form = BookForm(request.POST, request.FILES)
        book = form.save(commit=False)
        book.owner = request.user.profil
        book.slug = slugify(book.titre)
        book.save()
        return redirect("library")

     