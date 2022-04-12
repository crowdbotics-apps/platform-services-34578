from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


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
    first_name = models.CharField(
        max_length=15,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=15,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        max_length=30,
        null=True,
        blank=True,
    )
    phone = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    password = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        null=True,
        blank=True,
    )
    is_verified_at = models.BooleanField(
        null=True,
        blank=True,
    )
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
        return self.username
        # return "{first_name} {last_name}".format(first_name=self.first_name, last_name=self.last_name)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
