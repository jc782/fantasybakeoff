# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-02 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantasybakeoff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
