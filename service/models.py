from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

from django.utils.translation import gettext_lazy as _
from career.models import Vacancy
from portfolio.models import ServiceProject
from trustme_backend.utils.base_model import BaseModel


class ServiceCategory(BaseModel):
    question = models.CharField(max_length=200, verbose_name=_('Question'))
    answer = RichTextField(verbose_name=_('Answer'))

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = _('Service Category')
        verbose_name_plural = _('Service Categories')


class ServiceAdvantage(BaseModel):
    icon = models.ImageField(upload_to='advantages/', verbose_name=_('Icon'))
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = RichTextField(verbose_name=_('Description'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Service Advantage')
        verbose_name_plural = _('Service Advantages')


class ServiceSpecialist(BaseModel):
    name = models.CharField(max_length=200, verbose_name=_('Name'))
    description = RichTextField(verbose_name=_('Description'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Service Specialist')
        verbose_name_plural = _('Service Specialists')


class ServicePacket(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = RichTextField(verbose_name=_('Description'))
    price = models.IntegerField(verbose_name=_('Price'))
    price_per = models.CharField(max_length=200, verbose_name=_('Price per'))
    is_main = models.BooleanField(default=False, verbose_name=_('Is main'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Service Packet')
        verbose_name_plural = _('Service Packets')


class Service(BaseModel):
    title = models.CharField(max_length=200, null=True)
    short_description = models.TextField(null=True)
    full_description = RichTextField(null=True)
    icon = models.ImageField(null=True)
    categories = models.ManyToManyField(
        ServiceCategory, related_name='services_categories', blank=True)
    advantages = models.ManyToManyField(
        ServiceAdvantage, related_name='services_advantages', blank=True)
    specialists = models.ManyToManyField(
        ServiceSpecialist, related_name='services_specialists', blank=True)
    projects = models.ManyToManyField(
        ServiceProject, related_name='services_projects', blank=True)
    packets = models.ManyToManyField(
        ServicePacket, related_name='services_packets', blank=True)
    is_visible = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'service'
        verbose_name_plural = 'services'


class Applicant(BaseModel):
    full_name = models.CharField(max_length=255, verbose_name=_('Full name'))
    email = models.EmailField(
        max_length=255, verbose_name=_('Email'), null=True, blank=True)
    company_name = models.CharField(
        max_length=255, verbose_name=_('Company name'), null=True, blank=True)
    phone_prefix = models.CharField(
        max_length=255, verbose_name=_('Phone prefix'), null=True, blank=True)
    phone = models.CharField(max_length=255, verbose_name=_(
        'Phone'), null=True, blank=True)
    message = models.TextField(verbose_name=_(
        'Message'), null=True, blank=True)
    cv = models.FileField(upload_to='applicants/', null=True, blank=True)
    packet = models.ForeignKey(
        ServicePacket, on_delete=models.CASCADE, verbose_name=_('Packet'), null=True, blank=True)
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, verbose_name=_('Service'), null=True, blank=True)
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, verbose_name=_('Vacancy'), null=True, blank=True)
    project = models.ForeignKey(
        ServiceProject, on_delete=models.CASCADE, verbose_name=_('Project'), null=True, blank=True)
    site_link = models.URLField(max_length=255, verbose_name=_(
        'Site link'), null=True, blank=True)
    facebook_link = models.CharField(
        max_length=255, verbose_name=_('Facebook link'), null=True, blank=True)
    instagram_link = models.CharField(
        max_length=255, verbose_name=_('Instagram link'), null=True, blank=True)

    class Meta:
        db_table = 'applicant'
        verbose_name = _('Applicant')
        verbose_name_plural = _('Applicants')

    def __str__(self):
        return self.full_name
