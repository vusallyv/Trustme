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

STAR_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class Contact(BaseModel):
    full_name = models.CharField(max_length=255, verbose_name=_('Full name'))
    email = models.EmailField(max_length=255, verbose_name=_('Email'))
    company_name = models.CharField(
        max_length=255, verbose_name=_('Company name'))
    phone_prefix = models.IntegerField(verbose_name=_(
        'Phone prefix'), choices=PHONE_NUMBER_CHOICES, default='+994')
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
    type = models.IntegerField(verbose_name=_(
        'Type'), choices=VACANCY_TYPE_CHOICES, default='full_time')
    short_description = models.TextField(verbose_name=_('Short Description'))
    full_description = RichTextField(verbose_name=_('Full Description'))
    slug = models.SlugField(
        max_length=255, verbose_name=_('Slug'), unique=True)

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
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, verbose_name=_('Vacancy'))

    class Meta:
        db_table = 'applicant'
        verbose_name = _('Applicant')
        verbose_name_plural = _('Applicants')

    def __str__(self):
        return self.full_name


class AboutUs(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = RichTextField(verbose_name=_('Description'))
    aphorism = models.TextField(verbose_name=_('Aphorism'))
    aphorism_author = models.CharField(
        max_length=255, verbose_name=_('Aphorism author'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    class Meta:
        db_table = 'about_us'
        verbose_name = _('About Us')
        verbose_name_plural = _('About Us')

    def __str__(self):
        return self.title


class AboutUsStatistic(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    about_us = models.ForeignKey(
        AboutUs, on_delete=models.CASCADE, verbose_name=_('About Us'), related_name='about_us_statistic')

    class Meta:
        db_table = 'about_us_statistic'
        verbose_name = _('About Us Statistic')
        verbose_name_plural = _('About Us Statistic')

    def __str__(self):
        return self.title


class AboutUsInfo(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    icon = models.ImageField(upload_to='about_us_info', verbose_name=_('Icon'))
    mobile_icon = models.ImageField(
        upload_to='about_us_info', verbose_name=_('Mobile icon'))
    about_us = models.ForeignKey(
        AboutUs, on_delete=models.CASCADE, verbose_name=_('About Us'), related_name='about_us_info')

    class Meta:
        db_table = 'about_us_info'
        verbose_name = _('About Us Info')
        verbose_name_plural = _('About Us Info')

    def __str__(self):
        return self.title


class AboutUsTeam(BaseModel):
    full_name = models.CharField(max_length=255, verbose_name=_('Full name'))
    position = models.CharField(max_length=255, verbose_name=_('Position'))
    description = models.TextField(verbose_name=_('Description'))
    image = models.ImageField(
        upload_to='about_us_team', verbose_name=_('Image'))
    about_us = models.ForeignKey(
        AboutUs, on_delete=models.CASCADE, verbose_name=_('About Us'), related_name='about_us_team')

    class Meta:
        db_table = 'about_us_team'
        verbose_name = _('About Us Team')
        verbose_name_plural = _('About Us Team')

    def __str__(self):
        return self.full_name


class Testimonial(BaseModel):
    full_name = models.CharField(max_length=255, verbose_name=_('Full name'))
    company_name = models.CharField(
        max_length=255, verbose_name=_('Company name'))
    position = models.CharField(max_length=255, verbose_name=_('Position'))
    comment = models.TextField(verbose_name=_('Comment'))
    star = models.IntegerField(verbose_name=_(
        'Star'), choices=STAR_CHOICES, default=1)
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    class Meta:
        db_table = 'testimonial'
        verbose_name = _('Testimonial')
        verbose_name_plural = _('Testimonials')

    def __str__(self):
        return self.full_name
