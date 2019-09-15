from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .models import Produto

def index(request):
    produto = Produto.objects.all()
    return render(request, "index.html", {"produtos": produto,})

# def registration(request):


def sair(request):
    logout(request)
    return render(request, 'index.html')

