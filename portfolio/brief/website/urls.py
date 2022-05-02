from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path("brief", views.BriefView.as_view(), name="brief"),
]
