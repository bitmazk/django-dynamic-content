# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-08-05 01:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_content', '0003_auto_20150701_0755'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dynamiccontenttranslation',
            options={'default_permissions': (), 'managed': True},
        ),
    ]
