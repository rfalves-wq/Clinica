from datetime import date
from django.shortcuts import render, redirect, get_object_or_404

from pacientes.models import Paciente
from .models import Consulta
from triagem.forms import TriagemForm


# =========================
# MARCAR CONSULTA (RECEPÇÃO)
# =========================
def marcar_consulta(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == 'POST':
        Consulta.objects.create(
            paciente=paciente
        )
        return redirect('fila_espera')

    return render(request, 'consulta/marcar_consulta.html', {
        'paciente': paciente
    })


# =========================
# FILA DE TRIAGEM
# =========================
def fila_espera(request):
    consultas = Consulta.objects.filter(
        status='AGUARDANDO_TRIAGEM'
    )
    return render(request, 'consulta/fila_espera.html', {
        'consultas': consultas
    })


# =========================
# FILA DO MÉDICO
# =========================
def fila_medico(request):
    consultas = Consulta.objects.filter(
        status='AGUARDANDO_MEDICO'
    )
    return render(request, 'consulta/fila_medico.html', {
        'consultas': consultas
    })


# =========================
# MUDAR STATUS (UTILITÁRIO)
# =========================
def mudar_status(request, consulta_id, status):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    consulta.status = status
    consulta.save()
    return redirect('fila_espera')


# =========================
# ATENDIMENTO DO MÉDICO
# =========================
from django.shortcuts import render, get_object_or_404, redirect
from .models import Consulta
from triagem.forms import TriagemForm

from triagem.models import Triagem

from triagem.models import Triagem
from triagem.forms import TriagemForm

def atender_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)

    triagem, created = Triagem.objects.get_or_create(
        consulta=consulta
    )

    if request.method == 'POST':
        form = TriagemForm(request.POST, instance=triagem)
        if form.is_valid():
            form.save()
            consulta.status = 'FINALIZADA'
            consulta.save()
            return redirect('fila_medico')
    else:
        form = TriagemForm(instance=triagem)

    return render(request, 'consulta/atender_consulta.html', {
        'consulta': consulta,
        'form': form
    })

