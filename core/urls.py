from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name = "home"),
    path("faq", views.faq, name = "faq"),
    path("about-us", views.about_us, name = "about_us"),
    path("careers", views.VacancyListView.as_view(), name = "careers"),
    path("careers/<slug:slug>", views.VacancyDetailView.as_view(), name = "career-detail"),
    path("contact", views.ContactView.as_view(), name = "contact"),
]