from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    # WARNING!
    """
    Some officially supported features of Crowdbotics Dashboard depend on the initial
    state of this User model (Such as the creation of superusers using the CLI
    or password reset in the dashboard). Changing, extending, or modifying this model
    may lead to unexpected bugs and or behaviors in the automated flows provided
    by Crowdbotics. Change it at your own risk.


    This model represents the User instance of the system, login system and
    everything that relates with an `User` is represented by this model.
    """
    name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    first_name = models.TextField(
        null=True,
        blank=True,
    )
    last_name = models.TextField(
        null=True,
        blank=True,
    )
    phone = models.TextField(
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
        max_length=50,
    )
    password = models.TextField(
        null=True,
        blank=True,
    )
    email_verified_at = models.DateTimeField(
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        null=True,
        blank=True,
        auto_now=True,
    )
    updated_at = models.DateTimeField(
        null=True,
        blank=True,
        auto_now=True,
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
    )
    subscriptions = models.OneToOneField(
        "subscriptions.Subscriptions",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="user_subscriptions",
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
