from core.models import PHONE_NUMBER_CHOICES
from django import template
register = template.Library()


@register.simple_tag
def get_phone_prefixes():
    return PHONE_NUMBER_CHOICES