from rest_framework import serializers
from plan_features.models import PlanFeatures


class PlanFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanFeatures
        fields = "__all__"
