# Generated by Django 1.11.15 on 2018-11-06 05:24

import django.db.models.deletion
from django.db import migrations, models

import app.models
import sln_custom_storages as sln_custom_storages


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AppConfig",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "navigation_drawer_image",
                    models.FileField(
                        blank=True,
                        default=None,
                        null=True,
                        storage=sln_custom_storages.AppImageStorage(),
                        upload_to=app.models.image_path,
                    ),
                ),
            ],
            options={
                "verbose_name": "Android App Config",
                "verbose_name_plural": "Android App Config",
            },
        ),
        migrations.CreateModel(
            name="Nationality",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
                (
                    "flag",
                    models.FileField(
                        storage=sln_custom_storages.AppImageStorage(), upload_to=app.models.language_image_path
                    ),
                ),
            ],
            options={
                "verbose_name": "Nationality",
                "verbose_name_plural": "Nationalities",
            },
        ),
        migrations.CreateModel(
            name="Staff",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
                ("title", models.CharField(blank=True, max_length=200, null=True)),
                ("bio", models.CharField(blank=True, max_length=2048, null=True)),
                ("link", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "profile",
                    models.FileField(
                        storage=sln_custom_storages.AppImageStorage(), upload_to=app.models.profile_image_path
                    ),
                ),
            ],
            options={
                "verbose_name": "Staff",
                "verbose_name_plural": "Staff",
            },
        ),
        migrations.CreateModel(
            name="Translator",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
                ("link", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "nationality",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="translator",
                        to="app.Nationality",
                    ),
                ),
            ],
            options={
                "verbose_name": "Translator",
                "verbose_name_plural": "Translators",
            },
        ),
    ]
