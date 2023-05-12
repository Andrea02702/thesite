from django.shortcuts import render
from .models import post,image
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.core.paginator import Paginator



#pag post
class PostDetail(DetailView):
    model = post
    template_name = 'post/post.html'



#pag home
def jhome (request):
    Post = post.objects.all()
    paginator = Paginator(post.objects.all().order_by('-publis'),18)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'post/home.html',{'post':Post, 'posts':posts})



#pag atrezzatura
def atrezzatura(request):
    return render(request, 'post/atrezzatura.html')


#pag chi sono
def chi_sono(request):
    return render(request, 'post/chi_sono.html')


#pag tutti i post
def allpost (request):
    Post = post.objects.all()
    paginator = Paginator(post.objects.all().order_by('-publis'),18)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'post/allpost.html',{'post':Post, 'posts':posts})


#pag galleria
def galleria (request):
    Image = image.objects.all()
    paginator = Paginator(image.objects.all().order_by('-img_publis'),32)
    page = request.GET.get('page')
    images = paginator.get_page(page)

    return render(request, 'post/galleria.html',{'Image':Image, 'images':images})

#pag galleria
class foto(DetailView):
    model = image
    template_name = 'post/foto.html'