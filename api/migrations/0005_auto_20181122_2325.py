# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-22 23:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20181120_2035'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orbiter',
            new_name='OrbiterConfiguration',
        ),
    ]