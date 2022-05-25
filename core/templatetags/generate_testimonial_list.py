from service.models import Service
from django import template
register = template.Library()


@register.simple_tag
def generate_testimonial_list(star):    
    stars = []  
    for i in range(1, 6):
        if i <= star:
            stars.append(True)
        else:
            stars.append(False)
    return stars