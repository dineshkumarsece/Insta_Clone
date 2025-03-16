# Generated by Django 4.2.19 on 2025-03-04 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("profile_image", models.TextField()),
                ("nickname", models.CharField(max_length=24)),
                ("name", models.CharField(max_length=24)),
                ("email", models.CharField(max_length=24)),
            ],
            options={
                "db_table": "user",
            },
        ),
    ]
