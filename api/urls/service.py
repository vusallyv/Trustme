from django.urls import path
from api.views.service import PacketApplicantAPIView, ServiceApplicantAPIView

urlpatterns = [
    path("packet-applicant", PacketApplicantAPIView.as_view(), name="api-packet-applicant"),
    path("service-applicant", ServiceApplicantAPIView.as_view(), name="api-service-applicant"),
]