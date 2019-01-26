# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-20 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0009_spacecraftconfigurationtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='AstronautType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Astronaut Type',
                'verbose_name_plural': 'Astronaut Types',
            },
        ),
    ]