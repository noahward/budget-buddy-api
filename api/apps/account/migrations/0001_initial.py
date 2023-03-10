# Generated by Django 4.1.7 on 2023-02-21 16:05

from django.db import models, migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
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
                ("name", models.CharField(max_length=100)),
                ("nickname", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "kind",
                    models.CharField(
                        choices=[("spending", "spending"), ("saving", "saving")],
                        max_length=100,
                    ),
                ),
            ],
        ),
    ]
