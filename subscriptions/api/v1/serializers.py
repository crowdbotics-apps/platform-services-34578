from rest_framework import serializers
from subscriptions.models import Subscriptions


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = ("plan", "max_apps", "is_active")
        # fields = "__all__"
