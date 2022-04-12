from django.conf import settings
from django.db import models


class PlanFeatures(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    description = models.TextField()
    is_active = models.BooleanField()
    plan = models.ForeignKey(
        "plans.Plans",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="planfeatures_plan_id",
    )

    def __str__(self):
        return self.name


# Create your models here.
