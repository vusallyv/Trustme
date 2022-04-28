from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
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


class ProjectResult(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = RichTextField(verbose_name=_('Description'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Project Result')
        verbose_name_plural = _('Project Results')


class ProjectProcess(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    period = models.CharField(max_length=200, verbose_name=_('Period'))
    icon = models.ImageField(upload_to='process/', verbose_name=_('Icon'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Project Process')
        verbose_name_plural = _('Project Processes')


class ProjectImage(BaseModel):
    image = models.ImageField(upload_to='projects/', verbose_name=_('Image'))

    def __str__(self):
        return f"{self.image}"

    class Meta:
        verbose_name = _('Project Image')
        verbose_name_plural = _('Project Images')


class ServiceProject(BaseModel):
    url = models.URLField(verbose_name=_('URL'))
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = RichTextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='projects/', verbose_name=_('Image'))
    slug = models.SlugField(max_length=200, unique=True,
                            verbose_name=_('Slug'))
    process = models.ManyToManyField(
        ProjectProcess, related_name='project_process', verbose_name=_('Process'))
    results = models.ManyToManyField(
        ProjectResult, related_name='project_results', verbose_name=_('Results'))
    images = models.ManyToManyField(
        ProjectImage, related_name='project_images', verbose_name=_('Images'))

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Service Project')
        verbose_name_plural = _('Service Projects')


class ServicePacket(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = RichTextField(verbose_name=_('Description'))
    price = models.IntegerField(verbose_name=_('Price'))
    price_per = models.CharField(max_length=200, verbose_name=_('Price per'))

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
