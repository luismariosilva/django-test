from django.urls import path
from core import views



urlpatterns = [
    path('index/', views.index, name='index_page1'),
    path('livro/', views.lista_livros, name='list_livros'),
]