# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-01 18:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_staff_bio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='translator',
            old_name='language',
            new_name='nationality',
        ),
    ]