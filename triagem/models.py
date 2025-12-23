from django.db import models

class Triagem(models.Model):
    consulta = models.OneToOneField(
        'consulta.Consulta',
        on_delete=models.CASCADE
    )
    observacoes = models.TextField(blank=True)  # 👈 IMPORTANTE
