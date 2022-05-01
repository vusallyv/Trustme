from django.db import models

# Create your models here.

from trustme_backend.utils.base_model import BaseModel
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

VACANCY_TYPE_CHOICES = (
    (_('Full time'), _('Full time')),
    (_('Part time'), _('Part time')),
    (_('Internship'), _('Internship')),
)


class Vacancy(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    type = models.CharField(verbose_name=_(
        'Type'), choices=VACANCY_TYPE_CHOICES, default='full_time', max_length=255)
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
