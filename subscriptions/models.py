from django.conf import settings
from django.db import models


class Subscriptions(models.Model):
    "Generated Model"
    user_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="subscriptions_user_id",
    )
    plan_id = models.ForeignKey(
        "plans.Plans",
        on_delete=models.CASCADE,
        related_name="subscriptions_plan_id",
    )
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    status = models.CharField(
        null=True,
        blank=True,
        max_length=255
    )
    created_at = models.DateTimeField(
        auto_now=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    deleted_at = models.DateTimeField()


# Create your models here.
