from django import forms
from .models import Paciente


from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength': '14',
                'placeholder': '000.000.000-00',
                'oninput': 'mascaraCPF(this)'
            }),
        }

