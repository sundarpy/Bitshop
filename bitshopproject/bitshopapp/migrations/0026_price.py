# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-17 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitshopapp', '0025_new_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('upper_limit', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('lower_limit', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
            ],
        ),
    ]
