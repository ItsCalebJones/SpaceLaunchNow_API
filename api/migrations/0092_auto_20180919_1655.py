# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-19 20:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0091_auto_20180919_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firststage',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='firststage', to='configurations.FirstStageType'),
            preserve_default=False,
        ),
    ]
