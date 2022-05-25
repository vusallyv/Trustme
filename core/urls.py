from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name = "home"),
    path("faq", views.FAQView.as_view(), name = "faq"),
    path("about-us", views.AboutUsView.as_view(), name = "about_us"),
    path("contact", views.ContactView.as_view(), name = "contact"),
    path('set_language/', views.set_language, name="set_language")
]