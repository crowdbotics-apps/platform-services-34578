from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AppsViewSet

router = DefaultRouter()
router.register("apps", AppsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
