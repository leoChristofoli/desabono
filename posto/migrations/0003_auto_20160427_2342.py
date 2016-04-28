# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-27 23:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posto', '0002_auto_20160427_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='divida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_add', models.DateTimeField(null=True)),
                ('valor', models.FloatField(null=True)),
                ('vencimento', models.CharField(max_length=20, null=True)),
                ('descricao', models.CharField(max_length=8000, null=True)),
                ('citado', models.CharField(max_length=8000, null=True)),
                ('tipo_divida', models.CharField(choices=[('DV', 'Duplicidade'), ('CD', 'Cheque devolvido'), ('SD', 'Saldo devedor'), ('JP', 'Juros nao pagos'), ('OT', 'Outro')], default='OT', max_length=2, null=True)),
                ('termos', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='credor',
            name='descricao',
        ),
        migrations.AddField(
            model_name='credor',
            name='data_add',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='divida',
            name='credor_cnpj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posto.credor'),
        ),
    ]
