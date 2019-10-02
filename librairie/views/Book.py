from django.shortcuts import render
from ..models import Livre, Like
from django.views import View

class BookView(View):
	template_name = "library_detail.html"

	def get(self, request, slug):
	    book = Livre.objects.get(slug=slug)
	    lasts = Livre.objects.filter(owner=book.owner)[:3]
	    try:
	        like_value = Like.objects.get(what=book,
	            who=request.user.profil).like
	    except:
	        like_value = 0
	    return render(request, self.template_name, locals())
	 