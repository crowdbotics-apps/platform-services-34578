from django.db import models


class Subscriptions(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="subscriptions_user_id",
    )
    plan = models.ForeignKey(
        "plans.Plans",
        on_delete=models.CASCADE,
        related_name="subscriptions_plan_id",
    )
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return "{plan} ({start_at} - {end_at})".format(plan=self.plan.name, start_at=self.start_at.strftime("%d-%b-%y"),
                                                       end_at=self.end_at.strftime("%d-%b-%y"))

    def save(self, *args, **kwargs):
        super(Subscriptions, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created_at']

# Create your models here.
