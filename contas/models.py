# contas/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

#class LoginForm(AuthenticationForm):
#    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
 #   password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    cpf = models.CharField(max_length=14, unique=True)
    trocar_senha = models.BooleanField(default=True)  # 👈 NOVO

    def __str__(self):
        return f"{self.user.username} - {self.cpf}"

