from django import forms
from .models import Prescricao

class PrescricaoForm(forms.ModelForm):
    class Meta:
        model = Prescricao
        fields = ['medicamentos']

    medicamentos = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        required=False,
        label="Medicamentos prescritos"
    )
