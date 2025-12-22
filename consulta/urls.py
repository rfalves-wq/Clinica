from django.urls import path
from . import views

urlpatterns = [
    path('fila/', views.fila_espera, name='fila_espera'),
    path(
        'mudar-status/<int:consulta_id>/<str:status>/',
        views.mudar_status,
        name='mudar_status'
       
    ),
     path('marcar/<int:paciente_id>/', views.marcar_consulta, name='marcar_consulta'),
]
