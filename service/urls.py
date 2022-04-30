from django.urls import path
from . import views

app_name = "service"

urlpatterns = [
    path("brief", views.brief, name = "brief"),
    path("digital-audit", views.DigitalAuditView.as_view(), name = "digital-audit"),
    path("portfolio/<slug:slug>", views.PortfolioDetailView.as_view(), name = "portfolio-detail"),
    path("packets", views.packets, name = "packets"),
    path("portfolio", views.PortfolioListView.as_view(), name = "portfolio"),
    path("services/<slug:slug>", views.ServiceDetailView.as_view(), name = "service-detail"),
    path("services", views.ServicesListView.as_view(), name = "services"),
]