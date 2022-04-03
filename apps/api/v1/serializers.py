from rest_framework import serializers
from apps.models import Apps


class AppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apps
        fields = "__all__"
