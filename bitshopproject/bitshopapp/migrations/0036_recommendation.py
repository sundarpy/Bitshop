# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 08:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bitshopapp', '0035_limitedoffer_saleoffer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac_address', models.IntegerField(blank=True, default='0', null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bitshopapp.Product')),
            ],
        ),
    ]
