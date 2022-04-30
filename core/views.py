from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from core.forms import ContactForm
from core.models import AboutUs, Testimonial, Vacancy
from blog.models import Blog
from django.db.models import Count
from django.utils.translation import gettext_lazy as _, activate
from service.models import Service, ServiceProject

# Create your views here.


class HomeView(View):
    def get(self, request):
        context = {
            'title': _('Home'),
            'services': Service.objects.all(),
            'blogs': Blog.objects.all(),
            'about_us': AboutUs.objects.filter(is_active=True).last(),
            'services_categories': Service.objects.annotate(Count('projects')).order_by('-projects__count')[:3],
            'services_categories_for_mobile': Service.objects.annotate(Count('projects')).order_by('-projects__count'),
            'projects': ServiceProject.objects.all()[:5],
            'testimonials': Testimonial.objects.filter(is_active=True).order_by('star'),
        }
        return render(request, "home.html", context=context)


def faq(request):
    return render(request, "faq.html")


class AboutUsView(TemplateView):
    template_name = "about-us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('About Us')
        context['about_us'] = AboutUs.objects.filter(is_active=True).last()
        return context


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'careers.html'
    context_object_name = 'vacancies'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Careers')
        return context


class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'vacancy.html'
    context_object_name = 'vacancy'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


class ContactView(View):
    def get(self, request):
        context = {
            "title": _("Contact"),
            "form": ContactForm,
        }
        return render(request, "contact.html", context=context)


def set_language(request):
    if request.GET.get('lang'):
        activate(request.GET.get('lang'))
        response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        response.set_cookie('django_language', request.GET['lang'])
        return response