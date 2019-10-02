from django.shortcuts import redirect
from ..models import Livre
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class SupprimerView(LoginRequiredMixin, View):

	def get(self, request, slug):
	    book = Livre.objects.get(slug=slug)
	    if book.owner.user == request.user:
	        book.delete()
	    return redirect("library")
	 