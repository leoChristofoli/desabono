from __future__ import unicode_literals

from django.db import models
from posto.models import credor


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


class comentario(models.Model):
    divida = models.ForeignKey(divida,
                               on_delete=models.CASCADE)
    credor = models.ForeignKey(credor,
                               on_delete=models.CASCADE)
    coment = models.CharField(max_length=8000,
                              null=True)
    data_add = models.DateField(null=True)
