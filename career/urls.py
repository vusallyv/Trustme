from django.urls import path
from . import views

app_name = "career"

urlpatterns = [
    path("careers", views.VacancyListView.as_view(), name = "careers"),
    path("careers/<slug:slug>", views.VacancyDetailView.as_view(), name = "career-detail"),
]