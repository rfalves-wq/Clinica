from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
