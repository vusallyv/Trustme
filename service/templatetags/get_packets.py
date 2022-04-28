from service.models import ServicePacket
from django import template
register = template.Library()


@register.simple_tag
def get_packets_of_service(request):
    slug = request.resolver_match.kwargs.get('slug')
    return ServicePacket.objects.filter(services_packets__slug=slug)
