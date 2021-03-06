# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-04 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='credor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=2000, null=True)),
                ('cnpj', models.CharField(max_length=12, null=True, unique=True)),
                ('endereco', models.CharField(blank=True, max_length=8000, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('tipo', models.CharField(max_length=255, null=True)),
                ('ip_user', models.CharField(max_length=255, null=True)),
                ('data_add', models.DateTimeField(null=True)),
            ],
        ),
    ]
