from django.shortcuts import render, get_object_or_404, redirect
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

            # 🔁 muda o status
            consulta.status = 'AGUARDANDO_MEDICO'
            consulta.save()

            return redirect('fila_espera')
    else:
        form = TriagemForm()

    return render(request, 'triagem/realizar_triagem.html', {
        'consulta': consulta,
        'form': form
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
