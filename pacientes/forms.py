from django import forms
from .models import Paciente



class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            field: forms.TextInput(attrs={'class': 'form-control'})
            for field in ['nome', 'cpf']
        } | {
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
        }
