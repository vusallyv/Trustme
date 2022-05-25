from rest_framework import serializers

from django.utils.translation import gettext_lazy as _

from service.models import Applicant


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['full_name', 'email', 'company_name',
                  'phone_prefix', 'phone', 'message', 'cv', 'site_link', 'facebook_link', 'instagram_link', 'packet', 'service', 'vacancy', 'project']

    def validate_full_name(self, value):
        if len(value.split()) != 2:
            raise serializers.ValidationError(
                _('Ad, soyad düzgün daxil edin.'))
        return value
