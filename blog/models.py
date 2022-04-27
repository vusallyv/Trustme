from django.db import models

# Create your models here.

from django.db import models
from trustme_backend.utils.base_model import BaseModel
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Blog(BaseModel):
    image = models.ImageField(upload_to='blog/', verbose_name=_('Image'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    body = RichTextField(verbose_name=_('Body'))
    author = models.CharField(max_length=255, verbose_name=_('Author'))
    slug = models.SlugField(max_length=255, verbose_name=_('Slug'), unique=True, blank=True)

    class Meta:
        db_table = 'blog'
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')

    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)