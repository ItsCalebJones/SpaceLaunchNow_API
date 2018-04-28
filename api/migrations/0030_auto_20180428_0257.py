# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-28 02:57
from __future__ import unicode_literals

from django.db import migrations, models
import spacelaunchnow.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_auto_20180428_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='logo_url',
            field=models.FileField(default=None, null=True, storage=spacelaunchnow.storage_backends.LogoStorage(), upload_to=b''),
        ),
    ]
