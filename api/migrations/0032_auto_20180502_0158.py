# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-02 01:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_auto_20180502_0157'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LauncherDetail',
            new_name='Launcher',
        ),
    ]