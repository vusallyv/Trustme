from django.db.models.signals import post_save
from django.dispatch import receiver
from service.models import Service, ServiceProject
from django.utils.text import slugify


@receiver(post_save, sender=Service)
def create_service_slug(sender, instance, *args, **kwargs):
    old_slug = instance.slug
    new_slug = slugify(f"{instance.title}-{instance.id}")
    if old_slug != new_slug:
        instance.slug = new_slug
        instance.save()


@receiver(post_save, sender=ServiceProject)
def create_service_project_slug(sender, instance, *args, **kwargs):
    old_slug = instance.slug
    new_slug = slugify(f"{instance.title}-{instance.id}")
    if old_slug != new_slug:
        instance.slug = new_slug
        instance.save()