from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico
from .forms import MedicoForm
from consulta.models import Consulta


def medico_list(request):
    medicos = Medico.objects.all()
    return render(request, 'medico/medico_list.html', {
        'medicos': medicos
    })

def medico_create(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medico_list')
    else:
        form = MedicoForm()

    return render(request, 'medico/form.html', {
        'form': form
    })

def medico_update(request, pk):
    medico = get_object_or_404(Medico, pk=pk)

    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('medico_list')
    else:
        form = MedicoForm(instance=medico)

    return render(request, 'medico/form.html', {
        'form': form
    })

def medico_delete(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    medico.delete()
    return redirect('medico_list')

def iniciar_atendimento(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    consulta.status = 'EM_ATENDIMENTO'
    consulta.save()
    return redirect('fila_medico')
