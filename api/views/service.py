from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from api.serializers.service import ApplicantSerializer
from service.models import Applicant, Service


class ApplicantAPIView(CreateAPIView):
    serializer_class = ApplicantSerializer
    permission_classes = [permissions.AllowAny]
    model = Applicant

    def create(self, request, *args, **kwargs):
        service = request.data.get('service')
        packet = request.data.get('packet')
        vacancy = request.data.get('vacancy')
        project = request.data.get('project')
        if service:
            request.data['service'] = Service.objects.get(slug=service).id
        if packet:
            request.data['packet'] = packet
        if vacancy:
            request.data['vacancy'] = vacancy
        if project:
            request.data['project'] = project
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
