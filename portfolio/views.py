from django.shortcuts import render

# Create your views here.

from portfolio.models import ServiceProject
from django.views.generic import ListView, DetailView
from django.utils.translation import gettext_lazy as _
from service.models import Service


class PortfolioDetailView(DetailView):
    model = ServiceProject
    template_name = 'portfolio-detail.html'
    context_object_name = 'portfolio'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['recommended_projects'] = ServiceProject.objects.exclude(id=self.object.id)[
            :3]
        return context


class PortfolioListView(ListView):
    template_name = 'portfolio.html'
    context_object_name = 'portfolios'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Portfolio')
        context['services'] = Service.objects.filter(is_visible=True)
        context['portfolio_title'] = Service.objects.filter(slug=self.request.GET.get('service')).first().title if self.request.GET.get(
            'service') else _('Hamısı')
        return context

    def get_queryset(self):
        if self.request.GET.get('service'):
            slug = self.request.GET.get('service')
            service = Service.objects.get(slug=slug)
            return ServiceProject.objects.filter(services_projects=service)
        return ServiceProject.objects.all()
