from __future__ import unicode_literals

from django.db import models


class credor(models.Model):
    nome = models.CharField(max_length=2000,
                            null=True)
    cnpj = models.CharField(max_length=12,
                            null=True,
                            unique=True)
    endereco = models.CharField(max_length=8000,
                                blank=True,
                                null=True)
    email = models.EmailField(null=True)
    tipo = models.CharField(max_length=255,
                            null=True)
    ip_user = models.CharField(max_length=255,
                               null=True)
    data_add = models.DateTimeField(null=True)


class divida(models.Model):
    credor_cnpj = models.ForeignKey(credor,
                                    on_delete=models.CASCADE)
    data_add = models.DateTimeField(null=True)
    valor = models.FloatField(null=True)
    vencimento = models.CharField(max_length=20,
                                  null=True)
    descricao = models.CharField(max_length=8000,
                                 null=True)
    citado = models.CharField(max_length=8000,
                              null=True)

    DUPLICIDATE = 'DV'
    CHEQUE = 'CD'
    SALDO = 'SD'
    JUROS = 'JP'
    OUTRO = 'OT'
    tipo_choices = (
        (DUPLICIDATE, 'Duplicidade'),
        (CHEQUE, 'Cheque devolvido'),
        (SALDO, 'Saldo devedor'),
        (JUROS, 'Juros nao pagos'),
        (OUTRO, 'Outro'),
    )
    tipo_divida = models.CharField(max_length=2,
                                   null=True,
                                   choices=tipo_choices,
                                   default=OUTRO)
    termos = models.BooleanField(default=False)
