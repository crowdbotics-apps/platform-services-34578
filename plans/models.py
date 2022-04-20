from django.conf import settings
from django.db import models


class Plans(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=25,
    )
    amount = models.DecimalField(
        max_digits=30,
        decimal_places=2,
        blank=True,
        default=0,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    is_active = models.BooleanField()
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
