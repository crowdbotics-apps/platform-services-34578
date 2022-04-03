from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import PlansViewSet

router = DefaultRouter()
router.register("plans", PlansViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
