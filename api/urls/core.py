from django.urls import path
from api.views.core import ContactAPIView, ApplicantAPIView

urlpatterns = [
    path("contact", ContactAPIView.as_view(), name="api-contact"),
    path("applicant", ApplicantAPIView.as_view(), name="api-applicant"),
]