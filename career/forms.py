from django import forms
from django.forms import ModelForm
from service.models import Applicant
from django.forms.widgets import Textarea


class VacancyForm(ModelForm):
    class Meta:
        model = Applicant
        fields = ('full_name', 'message', 'cv', 'vacancy')

        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Ad və soyadınızı daxil edin'}),
            'message': forms.Textarea(attrs={'placeholder': 'Mesajınızı yazın'}),
            'cv': forms.FileInput(attrs={'class': 'file-input'}),
            'vacancy': forms.HiddenInput(),
        }

    def clean_cv(self):
        cv = self.cleaned_data['cv']
        if not cv:
            raise forms.ValidationError('CV yüklənməlidir')
        return cv

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        if not full_name or len(full_name.split(' ')) < 2:
            raise forms.ValidationError('Ad və soyadınızı daxil edin')
        return full_name
