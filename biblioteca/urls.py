from django.urls import path
from biblioteca import views


urlpatterns = [
    path('generos/', views.lista_generos, name='lista_generos'),
]
