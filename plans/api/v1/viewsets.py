from rest_framework import authentication
from plans.models import Plans
from .serializers import PlansSerializer
from rest_framework import viewsets


class PlansViewSet(viewsets.ModelViewSet):
    serializer_class = PlansSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Plans.objects.all()
