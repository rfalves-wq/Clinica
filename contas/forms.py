from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

from .models import UserProfile

#LOGIN
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuário")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

#RESET DE SENHA SIMPLES (POR USUÁRIO)
class SimplePasswordResetForm(forms.Form):
    username = forms.CharField(label="Usuário", max_length=150)
    new_password = forms.CharField(label="Nova senha", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirme a nova senha", widget=forms.PasswordInput)

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("new_password") != cleaned.get("confirm_password"):
            raise ValidationError("As senhas não coincidem.")
        return cleaned

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not User.objects.filter(username=username).exists():
            raise ValidationError("Usuário não encontrado.")
        return username

#CADASTRO DE USUÁRIO (CPF + SENHA)
class UsuarioCreateForm(forms.ModelForm):
    cpf = forms.CharField(label="CPF")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirme a senha", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("password") != cleaned.get("confirm_password"):
            raise ValidationError("As senhas não coincidem.")
        return cleaned

    def clean_cpf(self):
        cpf = self.cleaned_data.get("cpf")

        if not validar_cpf(cpf):
            raise ValidationError("CPF inválido.")

        if UserProfile.objects.filter(cpf=cpf).exists():
            raise ValidationError("Este CPF já está cadastrado.")

        return cpf

#EDITAR USUÁRIO (CPF)
class UsuarioUpdateForm(forms.ModelForm):
    cpf = forms.CharField(label="CPF")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.user:
            profile, _ = UserProfile.objects.get_or_create(user=self.user)
            self.fields['cpf'].initial = profile.cpf

    def save(self, commit=True):
        user = super().save(commit)
        profile, _ = UserProfile.objects.get_or_create(user=user)
        profile.cpf = self.cleaned_data['cpf']
        profile.save()
        return user

#RESET DE SENHA POR CPF (SEM LOGIN)
class ResetSenhaPorCPFForm(forms.Form):
    cpf = forms.CharField(label="CPF", max_length=14)
    new_password = forms.CharField(label="Nova senha", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirmar senha", widget=forms.PasswordInput)

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("new_password") != cleaned.get("confirm_password"):
            raise ValidationError("As senhas não coincidem.")
        return cleaned

    def clean_cpf(self):
        cpf = self.cleaned_data.get("cpf")

        if not UserProfile.objects.filter(cpf=cpf).exists():
            raise ValidationError("CPF não encontrado.")

        return cpf

#VALIDAÇÃO DE CPF (DÍGITOS VERIFICADORES)
def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig1 = (soma * 10) % 11
    dig1 = 0 if dig1 == 10 else dig1

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig2 = (soma * 10) % 11
    dig2 = 0 if dig2 == 10 else dig2

    return cpf[-2:] == f"{dig1}{dig2}"



###################
