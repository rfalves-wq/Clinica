from django.shortcuts import redirect, get_object_or_404
from pacientes.models import Paciente
from .models import Consulta

def marcar_consulta(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    Consulta.objects.create(
        paciente=paciente
    )

    return redirect('fila_espera')


from django.shortcuts import render
from .models import Consulta
from datetime import date

def fila_espera(request):
    consultas = Consulta.objects.filter(
        data=date.today()
    ).exclude(status='FINALIZADO').order_by('criado_em')

    return render(request, 'consulta/fila_espera.html', {
        'consultas': consultas
    })

from django.shortcuts import redirect, get_object_or_404
from .models import Consulta

def mudar_status(request, consulta_id, status):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    consulta.status = status
    consulta.save()
    return redirect('fila_espera')
