# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-16 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posto', '0003_auto_20160506_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credor',
            name='cnpj',
            field=models.CharField(max_length=18, null=True, unique=True),
        ),
    ]