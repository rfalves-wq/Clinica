from django.db import models

class Enfermeiro(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    coren = models.CharField(max_length=20, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome