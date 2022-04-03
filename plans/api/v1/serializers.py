from rest_framework import serializers
from plans.models import Plans


class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = "__all__"
