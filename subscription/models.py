from django.conf import settings
from django.db import models


class Subscription(models.Model):
    "Generated Model"
    used_id = models.BigIntegerField()
    plan_id = models.BigIntegerField()
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    created_at = models.DateTimeField(
        auto_now=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )


# Create your models here.
