from rest_framework import serializers

from django.utils.translation import gettext_lazy as _

from service.models import PacketApplicant, ServiceApplicant


class PacketApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacketApplicant
        fields = ['full_name', 'email', 'company_name', 'packet', 'service']

    def validate_full_name(self, value):
        if len(value.split()) != 2:
            raise serializers.ValidationError(
                _('Ad, soyad düzgün daxil edin.'))
        return value

class ServiceApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceApplicant
        fields = ['full_name', 'email', 'company_name', 'phone_prefix', 'phone', 'service']

    def validate_full_name(self, value):
        if len(value.split()) != 2:
            raise serializers.ValidationError(
                _('Ad, soyad düzgün daxil edin.'))
        return value
