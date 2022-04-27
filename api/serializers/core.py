from rest_framework import serializers

from core.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'company_name',
                  'phone_prefix', 'phone', 'message']

