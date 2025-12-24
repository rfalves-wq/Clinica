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
    consultas = Consulta.objects.filter(status='AGUARDANDO_MEDICO')
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

from django.shortcuts import render, get_object_or_404
from .models import Consulta
from triagem.models import Triagem

from django.shortcuts import render, get_object_or_404, redirect
from .models import Consulta, Prescricao
from triagem.models import Triagem
from .forms import PrescricaoForm

def atender_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    triagem = get_object_or_404(Triagem, consulta=consulta)

    # se já existir prescrição, reutiliza
    prescricao = getattr(consulta, 'prescricao', None)

    if request.method == 'POST':
        form = PrescricaoForm(request.POST, instance=prescricao)
        if form.is_valid():
            prescricao = form.save(commit=False)
            prescricao.consulta = consulta
            prescricao.save()

            consulta.status = 'FINALIZADA'
            consulta.save()

            return redirect('fila_medico')
    else:
        form = PrescricaoForm(instance=prescricao)

    return render(request, 'consulta/atender_consulta.html', {
        'consulta': consulta,
        'triagem': triagem,
        'form': form,   # 🔴 ISSO É O QUE FALTAVA
    })



from django.shortcuts import render, get_object_or_404, redirect
from .models import Consulta, Prescricao
from triagem.models import Triagem
from .forms import PrescricaoForm
def atendimento_medico(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    triagem = get_object_or_404(Triagem, consulta=consulta)

    # Se já existir prescrição, edita; senão cria nova
    prescricao, created = Prescricao.objects.get_or_create(
        consulta=consulta
    )

    if request.method == 'POST':
        form = PrescricaoForm(request.POST, instance=prescricao)
        if form.is_valid():
            form.save()

            # muda status da consulta
            consulta.status = 'FINALIZADA'
            consulta.save()

            return redirect('fila_medico')
    else:
        form = PrescricaoForm(instance=prescricao)

    return render(request, 'consulta/atendimento_medico.html', {
        'consulta': consulta,
        'triagem': triagem,
        'form': form
    })

def fila_medico_partial(request):
    consultas = Consulta.objects.filter(status='AGUARDANDO_MEDICO')
    return render(request, 'consulta/fila_medico_partial.html', {
        'consultas': consultas
    })
