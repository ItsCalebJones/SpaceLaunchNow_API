# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-07-18 18:33
from __future__ import unicode_literals

import api.models
import custom_storages
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0074_remove_launch_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='launch',
            name='image_url',
            field=models.ImageField(blank=True, default=None, null=True, storage=custom_storages.LaunchImageStorage(), upload_to=api.models.launch_image_path),
        ),
        migrations.AddField(
            model_name='launch',
            name='infographic_url',
            field=models.ImageField(blank=True, default=None, null=True, storage=custom_storages.LaunchImageStorage(), upload_to=api.models.infographic_image_path),
        ),
    ]
