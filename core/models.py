from django.db import models

# Create your models here.

from django.db import models
from trustme_backend.utils.base_model import BaseModel
from django.utils.translation import gettext_lazy as _

PHONE_NUMBER_CHOICES = (
    ('+994', '+994'),
    ('+7', '+7'),
    ('+1', '+1'),
)

class Contact(BaseModel):
    full_name = models.CharField(max_length=255, verbose_name=_('Full name'))
    email = models.EmailField(max_length=255, verbose_name=_('Email'))
    company_name = models.CharField(max_length=255, verbose_name=_('Company name'))
    phone_prefix = models.IntegerField(verbose_name=_('Phone prefix'), choices=PHONE_NUMBER_CHOICES, default='+994')
    phone = models.CharField(max_length=30, verbose_name=_('Phone'))
    message = models.TextField(verbose_name=_('Message'))

    class Meta:
        db_table = 'contact'
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __str__(self):
        return self.full_name