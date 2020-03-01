from django.shortcuts import render
from .models import Dono, Cliente, Funcionario
# Create your views here.

def index(request):
    clientes = Cliente.objects.all()
    funcionarios = Funcionario.objects.all()
    dado = {
        'cliente':clientes,
        'funcionario': funcionarios
    }
    return render(request,'index.html',dado)


def clientes(request):
    clientes = Cliente.objects.all()
    dados = {
        'cliente':clientes
    }
    return render(request, 'cliente.html', dados)