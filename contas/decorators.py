# contas/decorators.py
from django.shortcuts import redirect

def senha_definida_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if hasattr(request.user, 'profile') and request.user.profile.trocar_senha:
                return redirect('trocar_senha_por_cpf')
        return view_func(request, *args, **kwargs)
    return wrapper
