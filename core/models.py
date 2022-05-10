from django.db import models

# Create your models here.

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
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    class Meta:
        db_table = 'about_us'
        verbose_name = _('About Us')
        verbose_name_plural = _('About Us')

    def __str__(self):
        return self.title


class AboutUsSlogan(BaseModel):
    about_us = models.ForeignKey(
        AboutUs, on_delete=models.CASCADE, verbose_name=_('About us'), related_name='about_us_slogan')
    slogan = models.TextField(verbose_name=_('Slogan'))
    slogan_author = models.CharField(
        max_length=255, verbose_name=_('Slogan author'))
        
    class Meta:
        db_table = 'about_us_slogan'
        verbose_name = _('About Us Slogan')
        verbose_name_plural = _('About Us Slogan')

    def __str__(self):
        return self.slogan


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
    is_active = models.BooleanField(default=False, verbose_name=_('Is active'))

    class Meta:
        db_table = 'testimonial'
        verbose_name = _('Testimonial')
        verbose_name_plural = _('Testimonials')

    def __str__(self):
        return self.full_name


class ContactInfo(BaseModel):
    email = models.EmailField(verbose_name=_('Email'))
    address = models.TextField(verbose_name=_('Address'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    class Meta:
        db_table = 'contact_info'
        verbose_name = _('Contact Info')
        verbose_name_plural = _('Contact Info')

    def __str__(self):
        return self.email


class ContactPhone(BaseModel):
    phone_number = models.CharField(
        max_length=255, verbose_name=_('Phone number'))
    contact_info = models.ForeignKey(
        ContactInfo, on_delete=models.CASCADE, verbose_name=_('Contact info'), related_name='contact_phone')

    class Meta:
        db_table = 'contact_phone'
        verbose_name = _('Contact Phone')
        verbose_name_plural = _('Contact Phone')

    def __str__(self):
        return self.phone_number


class SocialLink(BaseModel):
    link = models.URLField(verbose_name=_('Link'))
    icon = models.ImageField(
        upload_to='social_link/', verbose_name=_('Icon'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    contact_info = models.ForeignKey(
        ContactInfo, on_delete=models.CASCADE, verbose_name=_('Contact info'), related_name='social_link')

    class Meta:
        db_table = 'social_link'
        verbose_name = _('Social Link')
        verbose_name_plural = _('Social Link')

    def __str__(self):
        return f"{self.link}"
