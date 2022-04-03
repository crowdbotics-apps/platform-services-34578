from django.conf import settings
from django.db import models


class Apps(models.Model):
    "Generated Model"
    name = models.TextField()
    description = models.TextField()
    is_active = models.BooleanField()
    user_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="apps_user_id",
    )
    created_at = models.DateTimeField(
        auto_now=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    deleted_at = models.DateTimeField()


# Create your models here.
