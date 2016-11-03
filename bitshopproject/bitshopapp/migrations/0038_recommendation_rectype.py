# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitshopapp', '0037_auto_20161102_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='rectype',
            field=models.CharField(blank=True, choices=[('P', 'Product Click'), ('S', 'Search Result')], max_length=2, null=True),
        ),
    ]