# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-24 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0066_auto_20180823_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launch',
            name='launcher',
            field=models.ManyToManyField(related_name='launch', to='api.Launcher'),
        ),
    ]
