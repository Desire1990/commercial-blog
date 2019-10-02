from django.shortcuts import redirect
from ..models import Like
from django.contrib.auth.decorators import login_required

@login_required#(redirect_field_name='login')
def like(request, slug, new_value):
    book = Livre.objects.get(slug=slug)
    try:
        like = Like.objects.get(what=book, who=request.user.profil)
    except:
        like = Like(what=book, who=request.user.profil)
    if like.like == new_value:
        like.like = 0
    else:
        like.like = new_value
    like.save()
    return redirect("book", slug=slug)
 