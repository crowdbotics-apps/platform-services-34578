import json
from datetime import datetime

from rest_framework import serializers
from dateutil.relativedelta import relativedelta
from django.forms.models import model_to_dict
from django.utils.timezone import make_aware
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
        # get current date
        start_at = make_aware(datetime.now())
        end_at = start_at + relativedelta(months=1)

        subscription_count = (
            Subscriptions.objects.filter(user=request.user)
                .filter(end_at__range=[start_at, end_at])
                .filter(is_active=True).count()
        )

        # terminate new subscription if an active subscription exists
        if subscription_count > 0:
            return response.Response({'data': {
                "error": "User already have an active subscription"
            }}, status=status.HTTP_403_FORBIDDEN)

        request_data = {
            "start_at": start_at,
            "end_at": end_at,
            "user": request.user,
            "plan": Plans.objects.get(id=request.data.get('plan')),
            "is_active": True,
        }

        # create record
        data = model_to_dict(Subscriptions.objects.create(**request_data))

        headers = self.get_success_headers(data)
        return response.Response(data, status=status.HTTP_201_CREATED, headers=headers)
