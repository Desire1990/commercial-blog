from django.shortcuts import  render, redirect, reverse, get_object_or_404
from .models import Post 
from django.forms import ModelForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
from .forms import PostForm

def article_attrs( post_obj, page ):
    try:
        slide1 = post_obj[0]
        slides = post_obj[1:3]
    except IndexError:
        slide1 = None
        slides = None
    pages        = Paginator( post_obj, 2 )
    page_content = pages.page( page )
    pagination   = pages.page_range
    nom_app      = "stores"
    return (nom_app, slide1, slides, pages, page_content)
@login_required   
def accueil( request ):
    mdel = Post
    nom_app    = "Articles"
    page_title = "Articles" 
    accueil    = True
    post   = Post.objects.all().order_by('-created_on')
    try:
        page = int( request.GET["page"] )
    except MultiValueDictKeyError:
        page = 1
    nom_app, slide1, slides, pages, page_content = article_attrs( post, page )
    return render( request, 'postcontent.html', locals() )



@login_required
def post_view(request, pk, template_name='stores/postdetail.html'):
    post= get_object_or_404(Post, pk=pk) 
    #post = Post.objects.all()   
    return render(request, template_name, {'post':post})



@login_required
def post_create(request, template_name='stores/postform.html'):
    model = Post
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('stores')
            # do something.
    else:
        form = PostForm()
    return render(request,template_name, {"form": form})



@login_required
def post_update(request, pk, template_name='stores/postform.html'):
    post= get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('stores')
    return render(request, template_name, {'form':form})


@login_required
def post_delete(request, pk, template_name='stores/postdelete.html'):
    post= get_object_or_404(Post, pk=pk)    
    if request.method=='POST':
        post.delete()
        return redirect('stores')
    return render(request, template_name, {'post':post})


