from django.shortcuts import render, redirect, get_object_or_404
from .models import Enfermeiro
from .forms import EnfermeiroForm

def enfermeiro_list(request):
    enfermeiros = Enfermeiro.objects.all()
    return render(request, 'enfermeiro/enfermeiro_list.html', {
        'enfermeiros': enfermeiros
    })

def enfermeiro_create(request):
    if request.method == 'POST':
        form = EnfermeiroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enfermeiro_list')
    else:
        form = EnfermeiroForm()

    return render(request, 'enfermeiro/form.html', {
        'form': form
    })

def enfermeiro_update(request, pk):
    enfermeiro = get_object_or_404(Enfermeiro, pk=pk)

    if request.method == 'POST':
        form = EnfermeiroForm(request.POST, instance=enfermeiro)
        if form.is_valid():
            form.save()
            return redirect('enfermeiro_list')
    else:
        form = EnfermeiroForm(instance=enfermeiro)

    return render(request, 'enfermeiro/form.html', {
        'form': form
    })

def enfermeiro_delete(request, pk):
    enfermeiro = get_object_or_404(Enfermeiro, pk=pk)
    enfermeiro.delete()
    return redirect('enfermeiro_list')
