from rest_framework import authentication, response, status, permissions
from plans.models import Plans
from .serializers import PlansSerializer
from rest_framework import viewsets


class PlansViewSet(viewsets.ModelViewSet):
    serializer_class = PlansSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Plans.objects.all()

    """
    Destroy a model instance.
    """

    def destroy(self, request, *args, **kwargs):
        # deactivate plan when destroy method is called
        data = {'is_active': False}
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return response.Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

