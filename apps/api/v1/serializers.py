from rest_framework import serializers
from apps.models import Apps


class AppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apps
        fields = ("name", "description", "type", "framework", "domain_name", "screenshot", "is_active", "subscription")
