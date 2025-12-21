from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('contas.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', include('contas.urls')),
    path('pacientes/', include('pacientes.urls')),
    path('consulta/', include('consulta.urls')),

]
