import json
from datetime import datetime

from dateutil.relativedelta import relativedelta
from rest_framework import authentication, permissions, response, status
from rest_framework import viewsets

from plans.models import Plans
from subscriptions.models import Subscriptions
from .serializers import SubscriptionsSerializer
from ...permissions import IsUser


class SubscriptionsViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )

    permission_classes = (IsUser, permissions.IsAuthenticated,)

    queryset = Subscriptions.objects.all()

    """
    List a queryset.
    """

    def list(self, request, *args, **kwargs):
        queryset = (self.filter_queryset(self.get_queryset())
                    .filter(user=request.user.pk))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)

    """
    Create a model instance.
    """

    def create(self, request, *args, **kwargs):
        data = {
            "start_at": datetime.now(),
            "end_at": datetime.now() + relativedelta(months=1),
            "user": request.user,
            "plan": Plans.objects.get(id=request.data.get('plan')),
            "max_apps": request.data.get('max_apps'),
            "is_active": True,
        }

        Subscriptions(**data).save()
        data = json.loads(json.dumps(data, indent=4, sort_keys=True, default=str))
        headers = self.get_success_headers(data)
        return response.Response(data, status=status.HTTP_201_CREATED, headers=headers)
