# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-07 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divida', '0011_auto_20160523_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='divida',
            name='ident_devedor_cleaned',
            field=models.CharField(max_length=100, null=True),
        ),
    ]