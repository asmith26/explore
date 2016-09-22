from django.conf.urls import url

from .views import PostsView


urlpatterns = [
    url(r'^$', PostsView.as_view()),
]
