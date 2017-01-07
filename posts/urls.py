from django.conf.urls import url

from .views import PostsView, PostDetailView


urlpatterns = [
    url(r'^$', PostsView.as_view(), name="post-list"),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name="post-detail"),
]
