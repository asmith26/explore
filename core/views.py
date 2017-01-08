from django.views.generic import TemplateView

from .mixins import PageMixin


class HomeView(PageMixin, TemplateView):
    template_name = "home.html"
    page = "home"


class AboutView(PageMixin, TemplateView):
    template_name = "about.html"
    page = "about"
