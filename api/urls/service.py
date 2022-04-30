from django.urls import path
from api.views.service import DigitalAuditApplicantAPIView, PacketApplicantAPIView, ServiceApplicantAPIView

urlpatterns = [
    path("packet-applicant", PacketApplicantAPIView.as_view(), name="api-packet-applicant"),
    path("service-applicant", ServiceApplicantAPIView.as_view(), name="api-service-applicant"),
    path("digital-audit-applicant", DigitalAuditApplicantAPIView.as_view(), name="api-digital-audit-applicant"),
]