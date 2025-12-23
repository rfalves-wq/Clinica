from django.db import models
from consulta.models import Consulta
from enfermeiro.models import Enfermeiro
from medico.models import Medico

class Triagem(models.Model):
    consulta = models.OneToOneField(
        Consulta,
        on_delete=models.CASCADE,
        related_name='triagem'
    )

    enfermeiro = models.ForeignKey(
        Enfermeiro,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    medico = models.ForeignKey(
        Medico,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    peso = models.FloatField(null=True, blank=True)
    altura = models.FloatField(null=True, blank=True)
    pressao = models.CharField(max_length=20, blank=True)
    observacoes = models.TextField(blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Triagem - Consulta {self.consulta.id}"
