from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import SubscriptionsViewSet

router = DefaultRouter()
router.register("subscriptions", SubscriptionsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
