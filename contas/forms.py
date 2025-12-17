from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



from django import forms
from django.contrib.auth.models import User

class SimplePasswordResetForm(forms.Form):
    username = forms.CharField(label="Usuário", max_length=150)
    new_password = forms.CharField(label="Nova senha", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirme a nova senha", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")
        if new_password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem")
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("Usuário não encontrado")
        return username



from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile

class UsuarioCreateForm(forms.ModelForm):
    cpf = forms.CharField(label='CPF')
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('confirm_password'):
            raise ValidationError('As senhas não coincidem.')
        return cleaned_data

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if UserProfile.objects.filter(cpf=cpf).exists():
            raise ValidationError('CPF já cadastrado.')
        return cpf



from django import forms
from django.contrib.auth.models import User
from contas.models import UserProfile

class UsuarioUpdateForm(forms.ModelForm):
    cpf = forms.CharField(label='CPF')

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


#####################
