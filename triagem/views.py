from django.shortcuts import render, get_object_or_404, redirect
from consulta.models import Consulta
from .forms import TriagemForm

def realizar_triagem(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)

    # 🔒 evita triagem duplicada
    if hasattr(consulta, 'triagem'):
        return redirect('fila_medico')

    if request.method == 'POST':
        form = TriagemForm(request.POST)
        if form.is_valid():
            triagem = form.save(commit=False)
            triagem.consulta = consulta
            triagem.save()

            # muda status da consulta
            consulta.status = 'AGUARDANDO_MEDICO'
            consulta.save()

            return redirect('fila_medico')
    else:
        form = TriagemForm()

    return render(request, 'triagem/realizar_triagem.html', {
        'consulta': consulta,
        'form': form
    })
