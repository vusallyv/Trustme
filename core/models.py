from django.db import models

# Create your models here.

from django.db import models
from trustme_backend.utils.base_model import BaseModel
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

PHONE_NUMBER_CHOICES = (
    ('+994', '+994'),
    ('+7', '+7'),
    ('+1', '+1'),
    ('+90', '+90'),
)



STAR_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)



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
    icon = models.ImageField(
        upload_to='about_us_info/', verbose_name=_('Icon'))
    mobile_icon = models.ImageField(
        upload_to='about_us_info/', verbose_name=_('Mobile icon'))
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
        upload_to='about_us_team/', verbose_name=_('Image'))
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
