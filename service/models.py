from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from trustme_backend.utils.base_model import BaseModel


class Category(BaseModel):
    question = models.CharField(max_length=200, verbose_name=_('Question'))
    answer = RichTextField(verbose_name=_('Answer'))

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Advantage(BaseModel):
    icon = models.ImageField(upload_to='advantages/', verbose_name=_('Icon'))
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = RichTextField(verbose_name=_('Description'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Advantage')
        verbose_name_plural = _('Advantages')


class Specialist(BaseModel):
    name = models.CharField(max_length=200, verbose_name=_('Name'))
    description = RichTextField(verbose_name=_('Description'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Specialist')
        verbose_name_plural = _('Specialists')


class Project(BaseModel):
    url = models.URLField(verbose_name=_('URL'))
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = RichTextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='projects/', verbose_name=_('Image'))
    slug = models.SlugField(max_length=200, unique=True,
                            verbose_name=_('Slug'))

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')


class Packet(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = RichTextField(verbose_name=_('Description'))
    price = models.IntegerField(verbose_name=_('Price'))
    price_per = models.CharField(max_length=200, verbose_name=_('Price per'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Packet')
        verbose_name_plural = _('Packets')


class Service(BaseModel):
    title = models.CharField(max_length=200, null=True)
    short_description = models.TextField(null=True)
    full_description = RichTextField(null=True)
    icon = models.ImageField(null=True)
    categories = models.ManyToManyField(
        Category, related_name='services_categories', blank=True)
    advantages = models.ManyToManyField(
        Advantage, related_name='services_advantages', blank=True)
    specialists = models.ManyToManyField(
        Specialist, related_name='services_specialists', blank=True)
    projects = models.ManyToManyField(
        Project, related_name='services_projects', blank=True)
    packets = models.ManyToManyField(
        Packet, related_name='services_packets', blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'service'
        verbose_name_plural = 'services'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)
