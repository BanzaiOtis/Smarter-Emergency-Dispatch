# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-18 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_auto_20171117_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ems_calls',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
