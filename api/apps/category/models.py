from django.db import models

from api.apps.user.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    detailed_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Categories"
        constraints = [
            models.UniqueConstraint(
                fields=["name", "detailed_name"], name="unique_category"
            )
        ]


class UserCategory(models.Model):
    name = models.CharField(max_length=100)
    detailed_name = models.CharField(max_length=100)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_categories"
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "User Categories"
        constraints = [
            models.UniqueConstraint(
                fields=["user_id", "name", "detailed_name"], name="unique_user_category"
            )
        ]
