from django.urls import path
from . import views

urlpatterns = [
    path('', views.enfermeiro_list, name='enfermeiro_list'),
    path('novo/', views.enfermeiro_create, name='enfermeiro_create'),
    path('editar/<int:pk>/', views.enfermeiro_update, name='enfermeiro_update'),
    path('excluir/<int:pk>/', views.enfermeiro_delete, name='enfermeiro_delete'),
]
