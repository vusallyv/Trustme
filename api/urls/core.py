from django.urls import path
from api.views.core import ContactAPIView

urlpatterns = [
    path("contact", ContactAPIView.as_view(), name="api-contact"),
]