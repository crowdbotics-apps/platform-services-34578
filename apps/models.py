from django.conf import settings
from django.db import models


class Apps(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=50,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="apps_user_id",
    )
    subscription = models.ForeignKey(
        "subscriptions.Subscriptions",
        on_delete=models.CASCADE,
        related_name="apps_subscription_id",
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    type = models.CharField(
        choices=(
            ('web', "Web"),
            ('mobile', "Mobile"),
        ),
        default="web",
        max_length=20,
    )
    framework = models.CharField(
        choices=(
            ('django', "Django"),
            ('react_native', "React Native"),
        ),
        default="django",
        max_length=20,
    )
    domain_name = models.CharField(
        null=True,
        blank=True,
        max_length=50,
    )
    screenshot = models.FileField(
        null=True,
        blank=True,
        max_length=100,
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

# Create your models here.
