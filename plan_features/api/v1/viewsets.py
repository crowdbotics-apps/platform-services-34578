from rest_framework import authentication
from plan_features.models import PlanFeatures
from .serializers import PlanFeaturesSerializer
from rest_framework import viewsets


class PlanFeaturesViewSet(viewsets.ModelViewSet):
    serializer_class = PlanFeaturesSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = PlanFeatures.objects.all()
