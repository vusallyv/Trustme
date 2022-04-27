from django.db import models

# Create your models here.

from django.db import models
from trustme_backend.utils.base_model import BaseModel
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.utils.text import slugify

PHONE_NUMBER_CHOICES = (
    ('+994', '+994'),
    ('+7', '+7'),
    ('+1', '+1'),
)

VACANCY_TYPE_CHOICES = (
    (1, 'Full time'),
    (2, 'Part time'),
    (3, 'Internship'),
)

class Contact(BaseModel):
    full_name = models.CharField(max_length=255, verbose_name=_('Full name'))
    email = models.EmailField(max_length=255, verbose_name=_('Email'))
    company_name = models.CharField(max_length=255, verbose_name=_('Company name'))
    phone_prefix = models.IntegerField(verbose_name=_('Phone prefix'), choices=PHONE_NUMBER_CHOICES, default='+994')
    phone = models.CharField(max_length=30, verbose_name=_('Phone'))
    message = models.TextField(verbose_name=_('Message'))

    class Meta:
        db_table = 'contact'
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __str__(self):
        return self.full_name


class Vacancy(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    type = models.IntegerField(verbose_name=_('Type'), choices=VACANCY_TYPE_CHOICES, default='full_time')
    short_description = models.TextField(verbose_name=_('Short Description'))
    full_description = RichTextField(verbose_name=_('Full Description'))
    slug = models.SlugField(max_length=255, verbose_name=_('Slug'), unique=True)

    class Meta:
        db_table = 'vacancy'
        verbose_name = _('Vacancy')
        verbose_name_plural = _('Vacancies')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Vacancy, self).save(*args, **kwargs)


class Applicant(BaseModel):
    full_name = models.CharField(max_length=255, verbose_name=_('Full name'))
    message = models.TextField(verbose_name=_('Message'))
    cv = models.FileField(upload_to='cv', verbose_name=_('CV'))
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, verbose_name=_('Vacancy'))

    class Meta:
        db_table = 'applicant'
        verbose_name = _('Applicant')
        verbose_name_plural = _('Applicants')

    def __str__(self):
        return self.full_name   