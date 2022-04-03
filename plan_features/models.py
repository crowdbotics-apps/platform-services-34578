from django.conf import settings
from django.db import models


class PlanFeatures(models.Model):
    "Generated Model"
    name = models.TextField()
    description = models.TextField()
    is_active = models.BooleanField()
    plan_id = models.ForeignKey(
        "plans.Plans",
        on_delete=models.CASCADE,
        related_name="planfeatures_plan_id",
    )


# Create your models here.
