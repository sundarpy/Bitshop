# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-09 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitshopapp', '0007_auto_20160804_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='offer_price',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='selling_price',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
