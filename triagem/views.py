from django.shortcuts import render, get_object_or_404, redirect
from consulta.models import Consulta
from .models import Triagem
from .forms import TriagemForm

def realizar_triagem(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)

    triagem, criada = Triagem.objects.get_or_create(
        consulta=consulta
    )

    if request.method == 'POST':
        form = TriagemForm(request.POST, instance=triagem)
        if form.is_valid():
            form.save()
            consulta.status = 'AGUARDANDO_MEDICO'
            consulta.save()
            return redirect('fila_espera')
    else:
        form = TriagemForm(instance=triagem)

    return render(request, 'triagem/realizar.html', {
        'form': form,
        'consulta': consulta
    })

from datetime import date

def fila_medico(request):
    consultas = Consulta.objects.filter(
        data=date.today(),
        status='AGUARDANDO_MEDICO'
    )

    return render(request, 'consulta/fila_medico.html', {
        'consultas': consultas
    })
