from django.shortcuts import render
from django.http import HttpResponse
from core.models import Livro, Autor

# Create your views here.

def index(request):
    context = {'nome': 'Luis Mario', 'curso': 'Programação'}
    return render(request, 'core/index.html', context)



def lista_livros(request):
    livro = Livro.objects.all()
    context = {'livros': livro}
    return render(request, 'core/livros.html', context)










