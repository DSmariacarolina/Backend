from django.shortcuts import render
from .models import Post

def listar_postagens(request):
    posts = Post.objects.all()
    return render(request, 'blog/listar_postagens.html', {'posts': posts})

# Create your views here.

