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


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UsuarioCreateForm, UsuarioUpdateForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UsuarioCreateForm
from .models import UserProfile

def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            UserProfile.objects.create(
                user=user,
                cpf=form.cleaned_data['cpf']
            )

            messages.success(request, 'Usuário cadastrado com sucesso.')
            return redirect('home')
    else:
        form = UsuarioCreateForm()

    return render(request, 'usuarios/usuario_form.html', {
        'form': form,
        'titulo': 'Cadastrar Usuário'
    })



from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def usuario_list(request):
    usuarios = User.objects.select_related('profile').all()
    return render(request, 'usuarios/usuario_list.html', {
        'usuarios': usuarios
    })



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UsuarioUpdateForm
from django.contrib.auth.decorators import login_required

@login_required
def usuario_update(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = UsuarioUpdateForm(request.POST, instance=user, user=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário atualizado com sucesso.')
            return redirect('usuario_list')
    else:
        form = UsuarioUpdateForm(instance=user, user=user)

    return render(request, 'usuarios/usuario_form.html', {
        'form': form,
        'titulo': 'Editar Usuário'
    })



@login_required
def usuario_delete(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Usuário removido com sucesso!')
        return redirect('usuario_list')

    return render(request, 'usuarios/usuario_confirm_delete.html', {
        'user': user
    })


#####

from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def trocar_senha_por_cpf(request):
    user = request.user

    # segurança extra
    if not hasattr(user, 'profile'):
        messages.error(request, 'CPF não cadastrado.')
        return redirect('home')

    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')
        confirmar = request.POST.get('confirmar')

        if senha != confirmar:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('trocar_senha_por_cpf')

        if cpf != user.profile.cpf:
            messages.error(request, 'CPF inválido.')
            return redirect('trocar_senha_por_cpf')

        user.set_password(senha)
        user.save()

        messages.success(request, 'Senha alterada com sucesso. Faça login novamente.')
        return redirect('login')

    return render(request, 'contas/trocar_senha.html')
