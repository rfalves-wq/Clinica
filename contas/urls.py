from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('resetar-senha/', views.simple_password_reset, name='simple_password_reset'),

    
]
