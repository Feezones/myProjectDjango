from django.shortcuts import render
from .models import Produto

def index (request):
    produtos = Produto.objects.all()
    #print(dir(request.user))
    #print(f"User:{request.user}")
    #if str(request.user) == 'AnonymousUser':
    #    teste = 'Usuario não logado'
    #else:
    #    teste = 'Usuario logado'
    context = {
        'curso' : 'programacao web com django',
        'outro' : 'so pra testar',
        'produtos' : produtos
    #    'logado' : teste
    }
    return render(request, 'index.html', context)

def contato(request):
        return render(request, 'contato.html')

def produto(request, pk):
    print(f'PK: {pk}')
    prod = Produto.objects.get(id=pk)

    context = {
        'produto' : prod
    }
    return render(request, 'produto.html', context)

def register(request):
    return render(request, 'register.html')