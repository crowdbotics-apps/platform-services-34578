from rest_framework import serializers
from subscriptions.models import Subscriptions


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = ("plan", "is_active")
        # fields = "__all__"
