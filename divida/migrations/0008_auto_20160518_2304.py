# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-18 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divida', '0007_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='divida',
            name='termos',
            field=models.BooleanField(default=True, verbose_name='Termos de uso'),
        ),
    ]