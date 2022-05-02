# Create your views here.

from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _

from portfolio.brief.website.models import ACTIVITY_SPHERE_CHOICES, DESIGN_CHOICES, LANGUAGE_CHOICES, PROJECT_PERIOD_CHOICES, REQUIREMENTS_CHOICES, WEBSITE_TYPE_CHOICES


class BriefView(TemplateView):
    template_name = "brief.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Brief')
        context['brief_choices'] = {
            'activity_sphere_choices': ACTIVITY_SPHERE_CHOICES,
            'website_type_choices': WEBSITE_TYPE_CHOICES,
            'language_choices': LANGUAGE_CHOICES,
            'project_period_choices': PROJECT_PERIOD_CHOICES,
            'design_choices': DESIGN_CHOICES,
            'requirements_choices': REQUIREMENTS_CHOICES,
        }
        return context
