from django.shortcuts import render

from service.models import Project, Service
from django.views.generic import ListView, DetailView
from django.utils.translation import gettext_lazy as _
# Create your views here.


def brief(request):
    return render(request, "brief.html")


def digital_audit(request):
    return render(request, "digital-audit.html")


class PortfolioDetailView(DetailView):
    model = Project
    template_name = 'portfolio-detail.html'
    context_object_name = 'portfolio'


def packets(request):
    return render(request, "packets.html")


class PortfolioListView(ListView):
    # model = Project
    template_name = 'portfolio.html'
    context_object_name = 'portfolios'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Portfolio')
        context['services'] = Service.objects.all()
        context['service_param'] = self.get_service_param()
        return context
    
    def get_queryset(self):
        if self.request.GET.get('service'):
            slug = self.request.GET.get('service')
            service = Service.objects.get(slug=slug)
            return Project.objects.filter(services_projects=service)
        return Project.objects.all()

    def get_service_param(self):
        return self.request.GET.get('service')


class ServicesListView(ListView):
    model = Service
    template_name = 'services.html'
    context_object_name = 'services'


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service-detail.html'
    context_object_name = 'service'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context
