# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-04 14:57
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fantasybakeoff', '0002_auto_20160802_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='id',
        ),
        migrations.AddField(
            model_name='league',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 8, 4, 14, 57, 17, 968596, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]