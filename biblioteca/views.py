from django.shortcuts import render
from biblioteca.models import Genero

# Create your views here.

def lista_generos(request):
    genero = Genero.objects.all()
    context = {'generos': genero}
    return render(request, 'biblioteca/lista_generos.html', context)

