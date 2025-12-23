from django.urls import path
from . import views

urlpatterns = [
    path('', views.medico_list, name='medico_list'),
    path('novo/', views.medico_create, name='medico_create'),
    path('editar/<int:pk>/', views.medico_update, name='medico_update'),
    path('excluir/<int:pk>/', views.medico_delete, name='medico_delete'),
    path('consulta/atender/<int:consulta_id>/', views.iniciar_atendimento, name='iniciar_atendimento'),

]
