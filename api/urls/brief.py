from django.urls import path
from api.views.brief import BriefAPIView

urlpatterns = [
    path("brief", BriefAPIView.as_view(), name="api-brief"),
]
