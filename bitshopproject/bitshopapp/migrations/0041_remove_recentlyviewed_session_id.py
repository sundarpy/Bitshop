# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-07 10:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitshopapp', '0040_recentlyviewed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recentlyviewed',
            name='session_id',
        ),
    ]