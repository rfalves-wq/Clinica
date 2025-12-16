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
