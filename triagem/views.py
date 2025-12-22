from django.shortcuts import render, get_object_or_404, redirect
from consulta.models import Consulta
from .forms import TriagemForm

def realizar_triagem(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)

    if request.method == 'POST':
        form = TriagemForm(request.POST)
        if form.is_valid():
            triagem = form.save(commit=False)
            triagem.consulta = consulta
            triagem.save()

            consulta.status = 'TRIAGEM'
            consulta.save()

            return redirect('fila_espera')
    else:
        form = TriagemForm()

    return render(request, 'triagem/form.html', {
        'form': form,
        'consulta': consulta
    })
