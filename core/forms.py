from django import forms
from django.forms import ModelForm

from core.models import Contact
from django.utils.translation import gettext_lazy as _

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'company_name',
                  'phone_prefix', 'phone', 'message']

    widgets = {
        'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
        'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company name'}),
        'phone_prefix': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Phone prefix'}),
        'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
        'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
    }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].label = _('Full name')
        self.fields['email'].label = _('Email')
        self.fields['company_name'].label = _('Company name')
        self.fields['phone_prefix'].label = _('Phone prefix')
        self.fields['phone'].label = _('Phone')
        self.fields['message'].label = _('Message')