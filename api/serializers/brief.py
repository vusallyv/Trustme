from django.utils.translation import gettext_lazy as _
from rest_framework import fields, serializers

from portfolio.brief.website.models import LANGUAGE_CHOICES, Brief


class BriefSerializer(serializers.HyperlinkedModelSerializer):
    language = fields.MultipleChoiceField(choices=LANGUAGE_CHOICES)

    class Meta:
        model = Brief
        fields = ['full_name', 'email', 'phone', 'phone_prefix', 'company_name', 'activity_sphere', 'website_url', 'new_domain',
                  'rival_website', 'liked_website', 'project_period', 'design', 'website_type', 'requirements', 'language']

    def validate_full_name(self, value):
        if len(value.split()) != 2:
            raise serializers.ValidationError(
                _('Ad, soyad düzgün daxil edin.'))
        return value
