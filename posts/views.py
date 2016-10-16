from django.views.generic.list import ListView
from django.views.generic import DetailView

from .models import Post


class PostsView(ListView):
    template_name = "posts/posts.html"
    model = Post


class PostDetailView(DetailView):
    template_name = "posts/post.html"
    model = Post
