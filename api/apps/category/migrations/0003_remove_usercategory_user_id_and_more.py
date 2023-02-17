# Generated by Django 4.1.7 on 2023-02-17 03:58

import django.db.models.deletion
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("transaction", "0003_remove_transaction_user_category_id"),
        ("category", "0002_alter_category_options_alter_usercategory_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usercategory",
            name="user_id",
        ),
        migrations.RemoveConstraint(
            model_name="category",
            name="unique_category",
        ),
        migrations.AddField(
            model_name="category",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_categories",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddConstraint(
            model_name="category",
            constraint=models.UniqueConstraint(
                fields=("user", "name", "detailed_name"), name="unique_user_category"
            ),
        ),
        migrations.DeleteModel(
            name="UserCategory",
        ),
    ]