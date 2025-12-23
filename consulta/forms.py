from django import forms
from .models import Prescricao

class PrescricaoForm(forms.ModelForm):
    class Meta:
        model = Prescricao
        fields = ['medicamento', 'dosagem', 'orientacoes']
