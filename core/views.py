from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from core.models import AboutUs, Testimonial
from blog.models import Blog
from django.db.models import Count
from django.utils.translation import gettext_lazy as _, activate
from service.models import Service, ServiceCategory, ServiceProject

# Create your views here.


class HomeView(View):
    def get(self, request):
        context = {
            'title': _('Home'),
            'services': Service.objects.filter(is_visible=True),
            'blogs': Blog.objects.all(),
            'about_us': AboutUs.objects.filter(is_active=True).last(),
            'services_categories': Service.objects.annotate(Count('projects')).order_by('-projects__count')[:3],
            'services_categories_for_mobile': Service.objects.annotate(Count('projects')).order_by('-projects__count'),
            'projects': ServiceProject.objects.all()[:5],
            'testimonials': Testimonial.objects.filter(is_active=True).order_by('star'),
        }
        return render(request, "home.html", context=context)


class FAQView(TemplateView):
    template_name = 'faq.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('FAQ')
        context['services'] = Service.objects.filter(is_visible=True)
        context['categories'] = self.get_queryset()
        return context

    def get_queryset(self):
        if self.request.GET.get('service'):
            return Service.objects.filter(is_visible=True, slug=self.request.GET.get('service')).first().categories.all()
        return ServiceCategory.objects.all()


class AboutUsView(TemplateView):
    template_name = "about-us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('About Us')
        context['about_us'] = AboutUs.objects.filter(is_active=True).last()
        return context


class ContactView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Contact')
        return context


def set_language(request):
    if request.GET.get('lang'):
        activate(request.GET.get('lang'))
        response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        response.set_cookie('django_language', request.GET['lang'])
        return response
