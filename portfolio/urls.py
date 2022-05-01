from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("portfolio/<slug:slug>", views.PortfolioDetailView.as_view(),
         name="portfolio-detail"),
    path("portfolio", views.PortfolioListView.as_view(), name="portfolio"),
]
