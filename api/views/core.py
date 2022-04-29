from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from api.serializers.core import ContactSerializer, ApplicantSerializer, TestimonialSerializer
from core.models import Contact, Applicant, Testimonial, Vacancy


class ContactAPIView(CreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]
    model = Contact


class TestimonialAPIView(CreateAPIView):
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.AllowAny]
    model = Testimonial


class ApplicantAPIView(CreateAPIView):
    serializer_class = ApplicantSerializer
    permission_classes = [permissions.AllowAny]
    model = Applicant

    def create(self, request, *args, **kwargs):
        vacancy = request.data.get('vacancy')
        request.data['vacancy'] = Vacancy.objects.get(slug=vacancy).id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
