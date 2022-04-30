from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from api.serializers.service import DigitalAuditApplicantSerializer, PacketApplicantSerializer, ServiceApplicantSerializer
from service.models import DigitalAuditApplicant, PacketApplicant, Service, ServiceApplicant


class PacketApplicantAPIView(CreateAPIView):
    serializer_class = PacketApplicantSerializer
    permission_classes = [permissions.AllowAny]
    model = PacketApplicant

    def create(self, request, *args, **kwargs):
        service = request.data.get('service')
        packet = request.data.get('packet')
        request.data['service'] = Service.objects.get(slug=service).id
        request.data['packet'] = packet
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ServiceApplicantAPIView(CreateAPIView):
    serializer_class = ServiceApplicantSerializer
    permission_classes = [permissions.AllowAny]
    model = ServiceApplicant

    def create(self, request, *args, **kwargs):
        service = request.data.get('service')
        request.data['service'] = Service.objects.get(id=service).id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DigitalAuditApplicantAPIView(CreateAPIView):
    serializer_class = DigitalAuditApplicantSerializer
    permission_classes = [permissions.AllowAny]
    model = DigitalAuditApplicant
