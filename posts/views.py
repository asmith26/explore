from django.views.generic.list import ListView
from django.views.generic import DetailView

from core.mixins import PageMixin
from .models import Post


class PostsView(PageMixin, ListView):
    template_name = "posts/posts.html"
    model = Post
    page = "posts"


class PostDetailView(PageMixin, DetailView):
    template_name = "posts/post.html"
    model = Post
    page = "posts"
