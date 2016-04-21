from __future__ import unicode_literals

from django.db import models


class credor(models.Model):
    nome = models.CharField(max_length=2000)
    cnpj = models.CharField(max_length=12)
    endereco = models.CharField(max_length=8000, blank=True)
    email = models.EmailField()
    tipo = models.CharField(max_length=255)
    responsavel = models.CharField(max_length=255)
    ip_user = models.CharField(max_length=255)
    descricao = models.CharField(max_length=8000)

