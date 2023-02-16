# Generated by Django 4.1.5 on 2023-02-15 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_portal"),
    ]

    operations = [
        migrations.CreateModel(
            name="JobDescription",
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
                ("role", models.CharField(max_length=250)),
                ("description_text", models.CharField(max_length=250)),
                ("pub_date", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name="portal",
            name="user",
        ),
        migrations.CreateModel(
            name="JobTitle",
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
                ("title", models.CharField(max_length=250)),
                (
                    "last_updated",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "job_description",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.jobdescription",
                    ),
                ),
                (
                    "portal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.portal"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Applicant",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("is_applicant", models.BooleanField(default=True)),
                ("cover_letter", models.CharField(max_length=250)),
                (
                    "applied_for",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.jobtitle"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("core.user",),
        ),
    ]
