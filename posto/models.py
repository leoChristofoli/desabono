# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class credor(models.Model):
    nome = models.CharField(
        max_length=2000,
        null=True
    )
    sobrenome = models.CharField(
        max_length=2000,
        null=True
    )
    cnpj = models.CharField(
        max_length=18,
        null=True,
        unique=True
    )
    empresa = models.CharField(
        max_length=1000,
        null=True,
        verbose_name='nome da empresa'
    )
    endereco = models.CharField(
        max_length=8000,
        blank=True,
        null=True,
        verbose_name='Endereço'
    )
    email = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE
    )
    tipo = models.CharField(
        max_length=255,
        null=True,
        verbose_name='Tipo da dívida'
    )
    ip_user = models.CharField(
        max_length=255,
        null=True
    )
    data_add = models.DateTimeField(
        null=True
    )
