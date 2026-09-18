from django.shortcuts import render

# Create your views here.

def meu_perfil(request):
    context = {'nome': 'Luis Mario', 'idade': '25', 'cidade': 'São Paulo', 'hobby': 'Programação'}
    return render(request, 'perfil/index.html', context)