# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-11 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posto', '0009_credor_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credor',
            name='tipo_empresa',
            field=models.CharField(choices=[('FAC', 'Factoring'), ('FDC', 'FIDC'), ('SEC', 'Securizadora'), ('OTR', 'Outro')], default='FAC', max_length=3, null=True, verbose_name='Tipo de empresa'),
        ),
    ]
