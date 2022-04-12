import json

from rest_framework import authentication, status, response, permissions
from apps.models import Apps
from subscriptions.models import Subscriptions
from .serializers import AppsSerializer
from ...permissions import IsUser, IsUserOrReadOnly
from rest_framework import viewsets


class AppsViewSet(viewsets.ModelViewSet):
    serializer_class = AppsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )

    permission_classes = (IsUser, permissions.IsAuthenticated, )

    queryset = Apps.objects.all()

    """
    List a queryset.
    """

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(user=request.user.pk)

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
            "name": request.data.get('name'),
            "description": request.data.get('description'),
            "type": request.data.get('type'),
            "framework": request.data.get('framework'),
            "screenshot": request.data.get('screenshot'),
            "domain_name": request.data.get('domain_name'),
            "user": request.user,
            "subscription": Subscriptions.objects.get(id=request.data.get('subscription')),
            "is_active": True,
        }

        Apps(**data).save()
        data.pop("user")
        data = json.loads(json.dumps(data, indent=4, sort_keys=True, default=str))
        headers = self.get_success_headers(data)
        return response.Response(data, status=status.HTTP_201_CREATED, headers=headers)