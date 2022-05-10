from django.db import models

# Create your models here.

from trustme_backend.utils.base_model import BaseModel
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

class ProjectStatistic(BaseModel):
    name = models.CharField(max_length=200, verbose_name=_('Name'))
    description = RichTextField(verbose_name=_('Description'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Project Statistic')
        verbose_name_plural = _('Project Statistics')


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
    aims = RichTextField(verbose_name=_('Aims'))
    cover_image = models.ImageField(
        upload_to='projects/', verbose_name=_('Cover Image'))
    slug = models.SlugField(max_length=200, unique=True,
                            verbose_name=_('Slug'))
    process = models.ManyToManyField(
        ProjectProcess, related_name='project_process', verbose_name=_('Process'), blank=True)
    results = models.ManyToManyField(
        ProjectResult, related_name='project_results', verbose_name=_('Results'), blank=True)
    images = models.ManyToManyField(
        ProjectImage, related_name='project_images', verbose_name=_('Images'), blank=True)
    statistics = models.ManyToManyField(
        ProjectStatistic, related_name='project_statistics', verbose_name=_('Statistics'), blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'service_project'
        verbose_name = _('Service Project')
        verbose_name_plural = _('Service Projects')

