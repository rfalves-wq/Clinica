from django.db import models

# Create your models here.
from django.db import models
from consulta.models import Consulta
from enfermeiro.models import Enfermeiro

class Triagem(models.Model):
    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE)
    enfermeiro = models.ForeignKey(Enfermeiro, on_delete=models.SET_NULL, null=True)
    pressao = models.CharField(max_length=10)
    temperatura = models.DecimalField(max_digits=4, decimal_places=1)
    observacoes = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Triagem - {self.consulta.paciente.nome}"
