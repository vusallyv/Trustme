from service.models import Service
from django import template
register = template.Library()


@register.simple_tag
def get_services():
    return Service.objects.filter(is_visible=True)
