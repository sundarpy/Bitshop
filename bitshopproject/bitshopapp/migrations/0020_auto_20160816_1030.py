# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-16 10:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitshopapp', '0019_auto_20160816_0855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcomment',
            old_name='subcomment',
            new_name='comment',
        ),
    ]
