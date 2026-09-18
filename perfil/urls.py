from django.urls import path
from perfil import views


urlpatterns = [
    path('eu/', views.meu_perfil, name='index1'),
]