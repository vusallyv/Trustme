from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from api.serializers.core import TestimonialSerializer
from core.models import Testimonial


class TestimonialAPIView(CreateAPIView):
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.AllowAny]
    model = Testimonial
