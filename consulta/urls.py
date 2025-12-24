from django.urls import path
from . import views

urlpatterns = [
    path('marcar/<int:paciente_id>/', views.marcar_consulta, name='marcar_consulta'),
    path('fila/', views.fila_espera, name='fila_espera'),
    path('fila-medico/', views.fila_medico, name='fila_medico'),
    path('atender/<int:consulta_id>/', views.atender_consulta, name='atender_consulta'),
    path('mudar-status/<int:consulta_id>/<str:status>/', views.mudar_status, name='mudar_status'),
     path('atender/<int:consulta_id>/', views.atender_consulta, name='atender_consulta'),
     path('fila-medico/atualizar/', views.fila_medico_partial, name='fila_medico_partial'),

]
