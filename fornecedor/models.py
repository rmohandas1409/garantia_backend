from django.db import models

class Fornecedor(models.Model):
    razao_social = models.CharField(max_length=100)
    cpf_cnpj = models.CharField(max_length=15)
    inscricao = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    endereco = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=5)
    cep = models.CharField(max_length=100)

    def __str__(self):
        return self.razao_social


