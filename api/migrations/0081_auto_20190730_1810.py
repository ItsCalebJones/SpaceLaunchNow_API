# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-30 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0080_launch_launch_service_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='launch_library_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
