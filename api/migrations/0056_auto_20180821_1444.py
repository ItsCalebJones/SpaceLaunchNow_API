# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-21 18:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0055_auto_20180821_1442'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LauncherInstance',
            new_name='Launcher',
        ),
    ]