from django.db import models
from medico.models import Medico
class Consulta(models.Model):

    STATUS_CHOICES = [
        ('AGUARDANDO', 'Aguardando'),
        ('TRIAGEM', 'Triagem'),
        ('ATENDIMENTO', 'Atendimento'),
        ('FINALIZADO', 'Finalizado'),
    ]

    paciente = models.ForeignKey(
        'pacientes.Paciente',
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='AGUARDANDO'
    )
    medico = models.ForeignKey(
        Medico,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    data = models.DateField(auto_now_add=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.paciente.nome} - {self.get_status_display()}'


