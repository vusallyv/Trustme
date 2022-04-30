from rest_framework import serializers

from django.utils.translation import gettext_lazy as _

from service.models import DigitalAuditApplicant, PacketApplicant, ServiceApplicant


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


class DigitalAuditApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalAuditApplicant
        fields = ['full_name', 'email', 'site_link', 'phone_prefix', 'phone', 'facebook_link', 'instagram_link']

    def validate_full_name(self, value):
        if len(value.split()) != 2:
            raise serializers.ValidationError(
                _('Ad, soyad düzgün daxil edin.'))
        return value
