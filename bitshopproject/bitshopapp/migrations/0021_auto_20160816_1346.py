# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-16 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitshopapp', '0020_auto_20160816_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='product',
        ),
        migrations.AddField(
            model_name='new',
            name='product_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
