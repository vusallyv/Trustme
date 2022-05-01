from django.shortcuts import render

from service.models import ServiceProject, Service
from django.views.generic import ListView, DetailView, TemplateView
from django.utils.translation import gettext_lazy as _
# Create your views here.


def brief(request):
    return render(request, "brief.html")


class DigitalAuditView(TemplateView):
    template_name = "digital-audit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['digital_audit'] = Service.objects.filter(
            slug__icontains='digital-audit').first()
        context['title'] = _('Digital Audit')
        return context


def packets(request):
    return render(request, "packets.html")


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
        context['services'] = Service.objects.filter(is_visible=True)
        return context
