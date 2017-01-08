from django.views.generic import TemplateView, View
from django.core.mail import send_mail

from braces import views

from .mixins import PageMixin


class HomeView(PageMixin, TemplateView):
    template_name = "home.html"
    page = "home"


class AboutView(PageMixin, TemplateView):
    template_name = "about.html"
    page = "about"


class ContactView(PageMixin, TemplateView):
    template_name = "contact.html"
    page = "contact"

class ContactSendView(views.CsrfExemptMixin, views.JsonRequestResponseMixin, View):
    require_json = True

    def post(self, request, *args, **kwargs):
        try:
            name = self.request_json["email"]
            name = self.request_json["name"]
            subject = self.request_json["subject"]
            message = self.request_json["message"]

            if not len(name) or not len(subject) or not len(message):
                raise KeyError
        except KeyError:
            error_dict = {"message": "you must include all fields"}
            return self.render_bad_request_response(error_dict)

        send_mail(subject, message, "myemail@mydomain.com", ["you@yourdomain.com"])

        return self.render_json_response(
            {"message": "Your contact has been sent!"})
