from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from django.utils.translation import gettext_lazy as _
from career.models import Vacancy

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

