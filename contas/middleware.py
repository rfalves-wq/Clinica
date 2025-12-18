# middleware.py
from django.shortcuts import redirect
from django.urls import reverse

class ForcarTrocaSenhaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if hasattr(request.user, 'userprofile'):
                if request.user.userprofile.trocar_senha:
                    # Evita loop infinito: permite acesso só à página de troca
                    if request.path != reverse('trocar_senha'):
                        return redirect('trocar_senha')
        response = self.get_response(request)
        return response
