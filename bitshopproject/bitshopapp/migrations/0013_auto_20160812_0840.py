# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-12 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitshopapp', '0012_category_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='icon',
            field=models.ImageField(blank=True, default='http://images.all-free-download.com/images/graphicthumb/abstract_led_tv_blank_screen_realistic_reflection_blue_wave_stylish_colorful_vector_6818232.jpg', null=True, upload_to='news/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, default='http://images.all-free-download.com/images/graphicthumb/abstract_led_tv_blank_screen_realistic_reflection_blue_wave_stylish_colorful_vector_6818232.jpg', null=True, upload_to='icons/'),
        ),
    ]
