from django.db import models

class Enfermeiro(models.Model):
    nome = models.CharField(max_length=100)
    coren = models.CharField(max_length=20, unique=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
