from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Paciente
from .forms import PacienteForm


from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
import re
from .models import Paciente

from django.db.models import Q, Case, When, IntegerField
from django.core.paginator import Paginator
import re

def listar_pacientes(request):
    termo = request.GET.get('busca', '').strip()
    pagina = request.GET.get('page', 1)

    pacientes = Paciente.objects.all()

    # Ordem da fila por status
    pacientes = pacientes.annotate(
        ordem_status=Case(
            When(status='AGUARDANDO', then=0),
            When(status='TRIAGEM', then=1),
            When(status='ATENDIMENTO', then=2),
            default=3,
            output_field=IntegerField()
        )
    ).order_by('ordem_status', 'criado_em')

    if termo:
        termo_limpo = re.sub(r'\D', '', termo)
        pacientes = pacientes.filter(
            Q(nome__icontains=termo) |
            Q(cpf__icontains=termo_limpo)
        )

    paginator = Paginator(pacientes, 10)
    page_obj = paginator.get_page(pagina)

    return render(request, 'pacientes/listar.html', {
        'pacientes': page_obj,
        'page_obj': page_obj,
        'termo': termo
    })




# ADICIONAR
def adicionar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/form.html', {'form': form})


# EDITAR
def editar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'pacientes/form.html', {'form': form})


# EXCLUIR
def excluir_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('listar_pacientes')
    return render(request, 'pacientes/confirmar_exclusao.html', {'paciente': paciente})


from django.shortcuts import redirect

def mudar_status(request, pk, status):
    paciente = get_object_or_404(Paciente, pk=pk)
    paciente.status = status
    paciente.save()
    return redirect('listar_pacientes')
