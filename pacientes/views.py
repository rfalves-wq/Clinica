from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Paciente
from .forms import PacienteForm


# LISTAR + BUSCA POR NOME/CPF
def listar_pacientes(request):
    termo = request.GET.get('busca', '').strip()

    pacientes = Paciente.objects.all()

    if termo:
        pacientes = pacientes.filter(
            Q(nome__icontains=termo) |
            Q(cpf__icontains=termo)
        )

    return render(request, 'pacientes/listar.html', {
        'pacientes': pacientes,
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
