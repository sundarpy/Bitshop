# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitshopapp', '0036_recommendation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='mac_address',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
