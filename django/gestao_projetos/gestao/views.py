from django.shortcuts import render
from .models import Projeto

def gestao_home(request):
    return render(request, 'gestao/index.html')

def listar_projetos(request):
    projetos = Projeto.objects.all()
    return render(
        request,
        'gestao/projetos.html',
        {'context' : projetos}
    )

