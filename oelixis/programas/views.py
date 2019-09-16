from django.contrib.auth import login, authenticate
from cuser.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Produto




def index(request):
    produto = Produto.objects.all()
    return render(request, "index.html", {"produtos": produto,})

# def registration(request):

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
    try:
        produto = Produto.objects.get(link=produto)
    except Produto.DoesNotExist:
        produto = None

    return render(request, 'produto.html', {'produto': produto,})