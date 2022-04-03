from rest_framework import authentication
from apps.models import Apps
from .serializers import AppsSerializer
from rest_framework import viewsets


class AppsViewSet(viewsets.ModelViewSet):
    serializer_class = AppsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Apps.objects.all()
