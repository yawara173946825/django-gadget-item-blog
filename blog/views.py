from django.shortcuts import render
from blog.models import Post,Category,Tag
from django.db.models import Count, Q
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
# Create your views here.

class PostListView(ListView):
    # 下記はqueryset = Post.objects.allと一緒
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
    
class CategoryListView(ListView):
    queryset = Category.objects.annotate(
        num_posts = Count('post', filter=Q(post__is_public=True))
    )

class TagListView(ListView):
    queryset = Tag.objects.annotate(
        num_posts = Count('post', filter=Q(post__is_public=True))
    )

class CategoryPostView(ListView):
    model = Post
    template_name = 'blog/category_post.html'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        self.category = get_object_or_404(Category, slug=category_slug)
        qs = super().get_queryset().filter(category=self.category)
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
    

    
    