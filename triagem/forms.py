from django import forms
from .models import Triagem

class TriagemForm(forms.ModelForm):
    class Meta:
        model = Triagem
        fields = [
            'peso',
            'altura',
            'pressao',
            'observacoes',
        ]
