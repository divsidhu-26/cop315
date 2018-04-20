# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-20 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noise', '0002_sensor_noise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='location',
        ),
        migrations.AddField(
            model_name='sensor',
            name='latitude',
            field=models.FloatField(default=28.542741),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensor',
            name='longitude',
            field=models.FloatField(default=77.193318),
            preserve_default=False,
        ),
    ]
