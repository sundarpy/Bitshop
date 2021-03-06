# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-10 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bitshopapp', '0009_remove_subcategory_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='SerfoProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('super_category', models.CharField(blank=True, choices=[('M', 'Men'), ('W', 'Women'), ('A', 'Appliances'), ('H', 'Home & Furniture'), ('E', 'Electronics')], max_length=2, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bitshopapp.Product')),
            ],
        ),
    ]
