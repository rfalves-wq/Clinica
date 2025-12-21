from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pacientes, name='listar_pacientes'),
    path('adicionar/', views.adicionar_paciente, name='adicionar_paciente'),
    path('editar/<int:pk>/', views.editar_paciente, name='editar_paciente'),
    path('excluir/<int:pk>/', views.excluir_paciente, name='excluir_paciente'),
    path('status/<int:pk>/<str:status>/', views.mudar_status, name='mudar_status'),
]
