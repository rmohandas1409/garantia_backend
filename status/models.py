from django.db import models

class Status(models.Model):
    TIPO = (
        ('A', 'Aberto'),
        ('PE', 'Pendente de envio'),
        ('PR', 'Pendente de retorno'),
        ('C', 'Concluido')
    )

    descricao = models.CharField(max_length=3, choices=TIPO, blank=False, null=False, default='A')

    def __str__(self):
        return self.descricao
