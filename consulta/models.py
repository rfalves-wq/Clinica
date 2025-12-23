from django.db import models
from pacientes.models import Paciente
from medico.models import Medico

class Consulta(models.Model):
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE
    )
    medico = models.ForeignKey(
        Medico,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=30,
        default='AGUARDANDO_TRIAGEM'
    )
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.paciente} - {self.status}"

from django.db import models
from .models import Consulta  # se estiver no mesmo app, ajuste se necessário

class Prescricao(models.Model):
    consulta = models.OneToOneField(
        Consulta,
        on_delete=models.CASCADE,
        related_name='prescricao'
    )

    medicamento = models.CharField(max_length=100)
    dosagem = models.CharField(max_length=100)
    orientacoes = models.TextField()

    def __str__(self):
        return f"Prescrição - {self.consulta}"


