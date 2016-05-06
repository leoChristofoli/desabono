# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-06 01:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='credor',
            name='sobrenome',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='credor',
            name='email',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]