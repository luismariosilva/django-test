from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import Livro, Autor
from core.forms import LivroForm

# Create your views here.

def index(request):
    context = {'nome': 'Luis Mario', 'curso': 'Programação'}
    return render(request, 'core/index.html', context)



def lista_livros(request):
    livro = Livro.objects.all()
    context = {'livros': livro}
    return render(request, 'core/livros.html', context)


from core.forms import LivroForm

def adicionar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm()
    
    return render(request, 'core/adicionar_livro.html', {'form': form})
        









