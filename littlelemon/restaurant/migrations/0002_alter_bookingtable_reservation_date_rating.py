# Generated by Django 4.2.6 on 2023-10-31 17:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookingtable",
            name="reservation_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 10, 31, 17, 46, 6, 474379, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.CreateModel(
            name="Rating",
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
                ("menuitem_id", models.SmallIntegerField()),
                ("rating", models.SmallIntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]