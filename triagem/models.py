from django.db import models
from consulta.models import Consulta

class Triagem(models.Model):
    consulta = models.OneToOneField(
        Consulta,
        on_delete=models.CASCADE
    )
    peso = models.FloatField()
    altura = models.FloatField()
    pressao = models.CharField(max_length=10)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"Triagem - {self.consulta.paciente}"
