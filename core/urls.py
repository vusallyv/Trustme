from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name = "home"),
    path("faq", views.faq, name = "faq"),
    path("about-us", views.AboutUsView.as_view(), name = "about_us"),
    path("careers", views.VacancyListView.as_view(), name = "careers"),
    path("careers/<slug:slug>", views.VacancyDetailView.as_view(), name = "career-detail"),
    path("contact", views.ContactView.as_view(), name = "contact"),
]