# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-27 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0011_auto_20190723_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='notification',
            name='title',
            field=models.TextField(max_length=32),
        ),
    ]