from django.conf.urls import url

from .views import HomeView, AboutView, ContactView, ContactSendView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^about/$', AboutView.as_view(), name="about"),
    url(r'^contact/$', ContactView.as_view(), name="contact"),
    url(r'^contact/send/$', ContactSendView.as_view(), name="contact-send"),
]
