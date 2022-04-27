from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from core.forms import ContactForm
from core.models import Vacancy
from django.utils.translation import gettext_lazy as _

# Create your views here.

def home(request):
    return render(request, "home.html")


def faq(request):
    return render(request, "faq.html")


def about_us(request):
    return render(request, "about-us.html")

class VacancyListView(ListView):
    model = Vacancy
    template_name = 'careers.html'
    context_object_name = 'vacancies'
    paginate_by = 6


class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'vacancy.html'
    context_object_name = 'vacancy'

class ContactView(View):
    def get(self, request):
        context = {
            "title": _("Contact"),
            "form": ContactForm,
        }
        return render(request, "contact.html", context=context)

    