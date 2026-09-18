from django.urls import path
from blog import views

urlpatterns = [
    path('sobre/', views.sobre, name='sobre_blog'),
    path('contato/', views.contato, name='contato_blog'),
]