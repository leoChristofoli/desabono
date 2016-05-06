from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class credor(models.Model):
    nome = models.CharField(max_length=2000,
                            null=True)
    sobrenome = models.CharField(max_length=2000,
                                 null=True)
    cnpj = models.CharField(max_length=12,
                            null=True,
                            unique=True)
    endereco = models.CharField(max_length=8000,
                                blank=True,
                                null=True)
    email = models.ForeignKey(User,
                              null=True,
                              on_delete=models.CASCADE)
    tipo = models.CharField(max_length=255,
                            null=True)
    ip_user = models.CharField(max_length=255,
                               null=True)
    data_add = models.DateTimeField(null=True)
