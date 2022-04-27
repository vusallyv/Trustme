from django.urls import path
from . import views

app_name = "service"

urlpatterns = [
    path("brief", views.brief, name = "brief"),
    path("design-service", views.design_service, name = "design-service"),
    path("digital-audit", views.digital_audit, name = "digital-audit"),
    path("digital-strategy-service", views.digital_strategy_service, name = "digital-strategy-service"),
    path("one-project", views.one_project, name = "one-project"),
    path("packets", views.packets, name = "packets"),
    path("portfolio", views.portfolio, name = "portfolio"),
    path("seo-service", views.seo_service, name = "seo-service"),
    path("services", views.services, name = "services"),
    path("smm-service", views.smm_service, name = "smm-service"),
    path("vacancy", views.vacancy, name = "vacancy"),
]