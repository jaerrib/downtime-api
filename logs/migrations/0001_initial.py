# Generated by Django 4.2.9 on 2024-01-25 23:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Log",
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
                ("customer_name", models.CharField(max_length=100)),
                ("assembly_number", models.CharField(max_length=100)),
                ("part_number", models.CharField(max_length=100)),
                ("lot_number", models.CharField(max_length=100)),
                ("date", models.DateField()),
                ("shift", models.IntegerField()),
                ("down_time", models.TimeField()),
                ("restart_time", models.TimeField()),
                ("problem", models.TextField()),
                ("root_cause", models.TextField()),
                ("corrective_action", models.TextField()),
                ("impact", models.TextField()),
                (
                    "initiator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
