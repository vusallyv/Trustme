from rest_framework import serializers

from core.models import Testimonial
from django.utils.translation import gettext_lazy as _


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['full_name', 'company_name', 'position', 'comment', 'star']

    def validate_full_name(self, value):
        if len(value.split()) != 2:
            raise serializers.ValidationError(
                _('Ad, soyad düzgün daxil edin.'))
        return value
