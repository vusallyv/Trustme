from django.urls import path
from api.views.core import TestimonialAPIView

urlpatterns = [
    path("testimonial", TestimonialAPIView.as_view(), name="api-testimonial"),
]
