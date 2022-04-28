from django.urls import path
from api.views.service import PacketApplicantAPIView

urlpatterns = [
    path("packet-applicant", PacketApplicantAPIView.as_view(), name="api-packet-applicant"),
]