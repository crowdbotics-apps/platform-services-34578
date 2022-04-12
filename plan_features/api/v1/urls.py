from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import PlanFeaturesViewSet

router = DefaultRouter()
router.register("plan_features", PlanFeaturesViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
