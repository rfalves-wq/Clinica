from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('resetar-senha/', views.simple_password_reset, name='simple_password_reset'),

     path('', views.home, name='home'),

    path('usuarios/', views.usuario_list, name='usuario_list'),
    path('usuarios/novo/', views.usuario_create, name='usuario_create'),
    path('usuarios/editar/<int:pk>/', views.usuario_update, name='usuario_update'),
    path('usuarios/excluir/<int:pk>/', views.usuario_delete, name='usuario_delete'),
    
]
