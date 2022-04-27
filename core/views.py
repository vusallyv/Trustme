from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from core.forms import ContactForm
from core.models import Vacancy
from blog.models import Blog
from django.utils.translation import gettext_lazy as _

from service.models import Service

# Create your views here.

class HomeView(View):
    def get(self, request):
        context = {
            'title': _('Home'),
            'services': Service.objects.all(),
            'blogs': Blog.objects.all(),
        }
        return render(request, "home.html", context=context)

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

    