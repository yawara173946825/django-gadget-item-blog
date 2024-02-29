from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    

    