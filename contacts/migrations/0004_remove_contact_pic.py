# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-30 13:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20170630_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='pic',
        ),
    ]
