from django.db import models

class Paciente(models.Model):

    STATUS_CHOICES = [
        ('AGUARDANDO', 'Aguardando'),
        ('TRIAGEM', 'Em Triagem'),
        ('ATENDIMENTO', 'Em Atendimento'),
    ]

    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=14)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='AGUARDANDO'
    )
    criado_em = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return self.nome
