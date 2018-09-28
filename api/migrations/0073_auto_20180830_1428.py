# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-30 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0072_auto_20180827_2019'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='launcher',
            options={'ordering': ['serial_number'], 'verbose_name': 'Launch Vehicle', 'verbose_name_plural': 'Launch Vehicles'},
        ),
        migrations.AddField(
            model_name='launcherconfig',
            name='fairing_diameter',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='launcherconfig',
            name='sso_capacity',
            field=models.IntegerField(blank=True, null=True, verbose_name='SSO Capacity (kg)'),
        ),
    ]
