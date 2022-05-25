from django.urls import path
from . import views

app_name = "service"

urlpatterns = [
    path("digital-audit", views.DigitalAuditView.as_view(), name = "digital-audit"),
    path("packets", views.packets, name = "packets"),
    path("services/<slug:slug>", views.ServiceDetailView.as_view(), name = "service-detail"),
    path("services", views.ServicesListView.as_view(), name = "services"),
]