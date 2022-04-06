from django.conf import settings
from django.db import models


class Plans(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=255
    )
    amount = models.DecimalField(
        max_digits=30,
        decimal_places=2,
    )
    is_active = models.BooleanField()


# Create your models here.
