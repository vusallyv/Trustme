from rest_framework import serializers

from core.models import Applicant, Contact
from django.utils.translation import gettext_lazy as _


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'company_name',
                  'phone_prefix', 'phone', 'message']

    def validate_full_name(self, value):
        if len(value.split()) != 2:
            raise serializers.ValidationError(
                _('Ad, soyad düzgün daxil edin.'))
        return value


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['full_name', 'message', 'cv', 'vacancy']

    def validate_full_name(self, value):
        if len(value.split()) != 2:
            raise serializers.ValidationError(
                _('Ad, soyad düzgün daxil edin.'))
        return value
