from django.db import models

# Create your models here.

from core.models import PHONE_NUMBER_CHOICES
from django.utils.translation import gettext_lazy as _
from trustme_backend.utils.base_model import BaseModel
from multiselectfield import MultiSelectField


ACTIVITY_SPHERE_CHOICES = (
    ('1', 'Activity 1'),
    ('2', 'Activity 2'),
    ('3', 'Activity 3'),
    ('4', 'Activity 4'),
    ('5', 'Activity 5'),
)

PROJECT_PERIOD_CHOICES = (
    ('2', '2 ay'),
    ('3', '3 ay'),
    ('6', '6 ay'),
    ('12', '12 ay'),
)

DESIGN_CHOICES = (
    ('1', 'Design 1'),
    ('2', 'Design 2'),
)

WEBSITE_TYPE_CHOICES = (
    ('1', 'E-commerce'),
    ('2', 'Blog'),
    ('3', 'Portal'),
    ('4', 'Sosial'),
    ('5', 'E-learning'),
)

REQUIREMENTS_CHOICES = (
    ('1', 'IOS'),
    ('2', 'Android'),
    ('3', 'Windows'),
    ('4', 'Mac'),
    ('5', 'Linux'),
)

LANGUAGE_CHOICES = (
    ('az', 'az'),
    ('en', 'en'),
    ('ru', 'ru'),
)


class Brief(BaseModel):
    full_name = models.CharField(max_length=200, verbose_name=_('Full Name'))
    email = models.EmailField(verbose_name=_('Email'))
    phone = models.CharField(max_length=200, verbose_name=_('Phone'))
    phone_prefix = models.CharField(max_length=200, verbose_name=_(
        'Phone Prefix'), choices=PHONE_NUMBER_CHOICES)
    company_name = models.CharField(
        max_length=200, verbose_name=_('Company Name'))
    activity_sphere = models.CharField(max_length=200, verbose_name=_(
        'Activity Sphere'), choices=ACTIVITY_SPHERE_CHOICES)
    website_url = models.URLField(verbose_name=_('Website URL'))
    new_domain = models.CharField(max_length=200, verbose_name=_(
        'New Domain'), blank=True, null=True)
    rival_website = models.TextField(verbose_name=_(
        'Rival Website'), blank=True, null=True)
    liked_website = models.TextField(verbose_name=_(
        'Liked Website'), blank=True, null=True)
    project_period = models.CharField(max_length=200, verbose_name=_(
        'Project Period'), choices=PROJECT_PERIOD_CHOICES)
    design = models.CharField(max_length=200, verbose_name=_(
        'Design'), choices=DESIGN_CHOICES)
    website_type = models.CharField(max_length=200, verbose_name=_(
        'Website Type'), choices=WEBSITE_TYPE_CHOICES)
    requirements = models.CharField(max_length=200, verbose_name=_(
        'Requirements'), choices=REQUIREMENTS_CHOICES)
    language = MultiSelectField(
        choices=LANGUAGE_CHOICES, verbose_name=_('Language'))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Brief'
        verbose_name_plural = 'Briefs'


class BriefPhoto(BaseModel):
    brief = models.ForeignKey(Brief, on_delete=models.CASCADE, verbose_name=_(
        'Brief'), related_name='brief_photo')
    photo = models.ImageField(verbose_name=_('Photo'))

    def __str__(self):
        return self.brief

    class Meta:
        verbose_name = 'Brief Photo'
        verbose_name_plural = 'Brief Photos'
