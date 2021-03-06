# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-11 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20171109_0606'),
    ]

    operations = [
        migrations.CreateModel(
            name='Current_ambulance',
            fields=[
                ('amb_id', models.IntegerField(primary_key=True, serialize=False)),
                ('LAT', models.FloatField()),
                ('LONG', models.FloatField()),
                ('AVAILABLE', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Current_emscall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LAT', models.FloatField()),
                ('LONG', models.FloatField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Current_predictions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zcta', models.CharField(max_length=5)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('day_of_month', models.IntegerField()),
                ('hour_of_day', models.IntegerField()),
                ('day_of_year', models.IntegerField()),
                ('week_of_year', models.IntegerField()),
                ('day_of_week', models.IntegerField()),
                ('is_weekend', models.BooleanField()),
                ('Call_counts', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='ems_calls',
            name='id',
        ),
        migrations.AddField(
            model_name='ems_calls',
            name='ems_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ambulance',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
