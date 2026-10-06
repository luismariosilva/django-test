from django.urls import path
from core import views



urlpatterns = [
    path('index/', views.index, name='index_page1'),
    path('livro/', views.lista_livros, name='lista_livros'),
    path('adicionar_livro/', views.adicionar_livro, name='adicionar_livro'),
    path('editar_livro/<int:livro_id>/', views.editar_livro, name='editar_livro'),
    path('apagar_livro/<int:livro_id>/', views.apagar_livro, name='apagar_livro'),
]