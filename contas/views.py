# contas/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # redireciona para a página principal
        else:
            messages.error(request, "Usuário ou senha inválidos")
    else:
        form = LoginForm()
    return render(request, 'contas/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SimplePasswordResetForm

def simple_password_reset(request):
    if request.method == "POST":
        form = SimplePasswordResetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            new_password = form.cleaned_data['new_password']
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            messages.success(request, "Senha redefinida com sucesso!")
            return redirect('login')
    else:
        form = SimplePasswordResetForm()
    return render(request, 'contas/simple_password_reset.html', {'form': form})
