# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class divida(models.Model):
    credor_cnpj = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='CNPJ do credor'
    )
    data_add = models.DateTimeField(
        null=True
    )
    valor = models.FloatField(
        null=True,
        verbose_name='Valor da divida'
    )
    nome_devedor = models.CharField(
        max_length=2000,
        null=True,
        verbose_name='nome do devedor'
    )
    ident_devedor = models.CharField(
        max_length=100,
        null=True,
        verbose_name='cnpj do devedor'
    )
    vencimento = models.DateField(
        null=True,
        verbose_name='Vencimento da dívida'
    )
    descricao = models.CharField(
        max_length=8000,
        null=True,
        verbose_name='Descrição'
    )
    citados = models.CharField(
        max_length=8000,
        null=True,
        verbose_name='Citados'
    )

    DUPLICIDATE = 'DV'
    CHEQUE = 'CD'
    SALDO = 'SD'
    JUROS = 'JP'
    OUTRO = 'OT'
    tipo_choices = (
        (DUPLICIDATE, 'Duplicata'),
        (CHEQUE, 'Cheque devolvido'),
        (SALDO, 'Saldo devedor'),
        (JUROS, 'Juros não pagos'),
        (OUTRO, 'Outro'),
    )
    tipo_divida = models.CharField(
        max_length=2,
        null=True,
        choices=tipo_choices,
        default=OUTRO,
        verbose_name='Tipo de dívida'
    )
    is_open = models.BooleanField(
        default=True,
        verbose_name='dívida ativa'
    )
    termos = models.BooleanField(
        default=True,
        verbose_name='Termos de uso'
    )
    ident_devedor_cleaned = models.CharField(
        max_length=100,
        null=True,
    )

    def save(self, *args, **kwargs):
        self.ident_devedor_cleaned = self.ident_devedor.replace('/', '').replace('.', '').replace('-', '')
        super(divida, self).save(*args, **kwargs)

    def __str__(self):
        return "{id}, {nome}".format(id=self.id, nome=self.nome_devedor)


class comentario(models.Model):
    divida = models.ForeignKey(
        divida,
        on_delete=models.CASCADE
    )
    credor = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    coment = models.CharField(
        max_length=8000,
        null=True,
        verbose_name='Descrição'
    )
    data_add = models.DateField(
        null=True
    )
    foi_paga = models.BooleanField(
        default=False,
        verbose_name='Foi paga'
    )
