from django.urls import path
from core import views



urlpatterns = [
    path('index/', views.index, name='index_page1'),
    path('livro/', views.lista_livros, name='lista_livros'),
    path('adicionar_livro/', views.adicionar_livro, name='adicionar_livro'),
]