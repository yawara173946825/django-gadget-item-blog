from django.urls import path
from blog.views import PostListView, PostDetailView, CategoryListView, TagListView, CategoryPostView, TagPostView

app_name = 'blog'
urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('category/<str:category_slug>/', CategoryPostView.as_view(), name ='category_post'),
    path('tag/<str:tag_slug>/', TagPostView.as_view(), name = 'tag_post'),
]