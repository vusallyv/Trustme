from django.urls import path
from api.views.service import ApplicantAPIView

urlpatterns = [
    path("applicant", ApplicantAPIView.as_view(), name="api-applicant"),
]