from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=150, default='')
    nascimento = models.CharField(max_length=100, default='')
    cpf = models.CharField(max_length=20, unique=True, default='')
    cidade = models.CharField(max_length=100, default='')
    genero = models.CharField(max_length=100, default='')
    estado = models.CharField(max_length=100, default='')
    telefone = models.CharField(max_length=14, default='')
    email = models.EmailField(max_length=150, unique=True, default='')
    confirmarEmail = models.CharField(max_length=150, default='')
    senha = models.CharField(max_length=150, default='')
    confirmarSenha = models.CharField(max_length=150, default='')
    aceitarTermos = models.BooleanField(max_length=3, default=True)

    def __str__(self):
        return self.nome
