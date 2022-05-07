# Create your views here.
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView
from django.utils.translation import gettext_lazy as _
from career.forms import VacancyForm
from career.models import Vacancy
from service.models import Applicant


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'careers.html'
    context_object_name = 'vacancies'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Careers')
        return context


class VacancyDetailView(DetailView, CreateView):
    form_class = VacancyForm
    template_name = 'vacancy.html'
    context_object_name = 'vacancy'
    model = Vacancy

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Vacancy.objects.get(slug=self.kwargs['slug']).title
        return context

    def post(self, request, *args, **kwargs):
        self.object = Vacancy.objects.get(slug=self.kwargs['slug'])
        form = self.get_form()
        if form.is_valid():
            # form.cleaned_data['vacancy'] = self.object
            # applicant = Applicant.objects.create(**form.cleaned_data)
            applicant = Applicant.objects.create(
                full_name=form.cleaned_data['full_name'],
                vacancy=self.object,
                message=form.cleaned_data['message'],
                cv=form.cleaned_data['cv'],
            )
            applicant.save()
            messages.success(request, _('Your application has been sent successfully.'))
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return '/careers/{}'.format(self.kwargs['slug'])
