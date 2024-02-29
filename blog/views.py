from django.shortcuts import render
from blog.models import Post
from django.http import Http404
from django.views.generic import ListView, DetailView
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.is_public and not self.request.user.is_authenticated:
            raise Http404
        return obj
    