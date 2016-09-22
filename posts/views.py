from django.views.generic.list import ListView

from .models import Post


class PostsView(ListView):
    template_name = "posts/posts.html"
    model = Post
