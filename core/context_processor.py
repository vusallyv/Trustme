from core.models import ContactInfo
from service.models import Service
def context_renderer(request):
    return {
       'services_footer': Service.objects.filter(is_visible=True),
       'contact_footer': ContactInfo.objects.filter(is_active=True).last(),
    }