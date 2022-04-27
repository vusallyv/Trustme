from django.shortcuts import render
from django.views import View

from core.forms import ContactForm
from django.utils.translation import gettext_lazy as _

# Create your views here.

def home(request):
    return render(request, "home.html")


def faq(request):
    return render(request, "faq.html")


def about_us(request):
    return render(request, "about-us.html")

def careers(request):
    return render(request, "careers.html")


class ContactView(View):
    def get(self, request):
        context = {
            "title": _("Contact"),
            "form": ContactForm,
        }
        return render(request, "contact.html", context=context)

    