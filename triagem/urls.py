from django.urls import path
from . import views

urlpatterns = [
    path('realizar/<int:consulta_id>/', views.realizar_triagem, name='realizar_triagem'),
]
