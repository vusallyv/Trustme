from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name = "home"),
    path("faq", views.faq, name = "faq"),
    path("about-us", views.about_us, name = "about_us"),
    path("careers", views.careers, name = "careers"),
    path("contact", views.contact, name = "contact"),
]