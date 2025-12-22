from django import forms
from .models import Enfermeiro

class EnfermeiroForm(forms.ModelForm):
    class Meta:
        model = Enfermeiro
        fields = ['nome', 'cpf', 'coren']
