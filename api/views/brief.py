from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from api.serializers.brief import BriefSerializer
from portfolio.brief.website.models import Brief


class BriefAPIView(CreateAPIView):
    serializer_class = BriefSerializer
    permission_classes = [permissions.AllowAny]
    model = Brief

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
