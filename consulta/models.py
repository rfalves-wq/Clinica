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
