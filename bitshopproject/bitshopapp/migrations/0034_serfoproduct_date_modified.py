# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-22 11:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitshopapp', '0033_auto_20160819_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='serfoproduct',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
