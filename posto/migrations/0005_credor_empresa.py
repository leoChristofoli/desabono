# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-19 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posto', '0004_auto_20160516_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='credor',
            name='empresa',
            field=models.CharField(max_length=1000, null=True, verbose_name='nome da empresa'),
        ),
    ]
