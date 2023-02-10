# Generated by Django 4.1.6 on 2023-02-10 00:15

import django.db.models.deletion
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("category", "0001_initial"),
        ("account", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("description", models.CharField(max_length=255)),
                ("currency_code", models.CharField(max_length=3)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=12)),
                (
                    "account_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.account",
                    ),
                ),
                (
                    "category_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="category.category",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
