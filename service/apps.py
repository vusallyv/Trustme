from django.apps import AppConfig


class ServiceConfig(AppConfig):
    name = 'service'

    def ready(self):
        from service.signals import create_service_slug, create_service_project_slug