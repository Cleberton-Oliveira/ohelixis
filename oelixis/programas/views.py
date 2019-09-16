from django.shortcuts import render
from django.contrib.auth import logout

from .models import Produto

def index(request):
    produto = Produto.objects.all()
    return render(request, "index.html", {"produtos": produto,})

# def registration(request):


def sair(request):
    logout(request)
    return render(request, 'index.html')


def produtoSelecionado(request, produto):
    try:
        produto = Produto.objects.get(link=produto)
    except Produto.DoesNotExist:
        produto = None

    return render(request, 'produto.html', {'produto': produto,})