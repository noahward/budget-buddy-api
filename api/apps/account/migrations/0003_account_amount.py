# Generated by Django 4.1.7 on 2023-03-06 00:53

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="amount",
            field=models.FloatField(default=1518.91),
            preserve_default=False,
        ),
    ]
