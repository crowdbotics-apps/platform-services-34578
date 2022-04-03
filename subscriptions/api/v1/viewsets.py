from rest_framework import authentication
from subscriptions.models import Subscriptions
from .serializers import SubscriptionsSerializer
from rest_framework import viewsets


class SubscriptionsViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Subscriptions.objects.all()
