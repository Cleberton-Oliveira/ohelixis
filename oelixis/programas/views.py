from django.contrib.auth import login, authenticate
from cuser.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Produto, Vendas
from .forms import VendaForm

def index(request):
    produto = Produto.objects.filter(vendido=False)
    return render(request, "index.html", {"produtos": produto,})

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


def sair(request):
    logout(request)
    return render(request, 'index.html')


def produtoSelecionado(request, produto):

    if request.method == "POST":
        print('passei')
        form = VendaForm(request.POST)
        produto = Produto.objects.get(link=produto)
        if form.is_valid():
            post = form.save(commit=False)
            produto.vendido = True
            produto.save()
            post.save()
            return redirect('/')
    else:
        form = VendaForm()
        produto = Produto.objects.get(link=produto)
        try:
            produto
        except Produto.DoesNotExist:
            produto = None
        form.initial = {'vendedor': produto.responsavel, 'comprador' : request.user, 'produto_vendido': produto}
        form.vendedor = produto.responsavel
        form.comprador = request.user
        form.produto_vendido = produto
        return render(request, 'produto.html', {'produto': produto, 'form': form})