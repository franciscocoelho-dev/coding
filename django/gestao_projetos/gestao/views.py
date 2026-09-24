from django.shortcuts import render
from .models import Projeto
from .forms import ProjetoForm

def gestao_home(request):
    return render(request, 'gestao/index.html')

def listar_projetos(request):
    projetos = Projeto.objects.all()
    return render(
        request,
        'gestao/projetos.html',
        {'context' : projetos}
    )

def adicionar_projetos(request):
    form = ProjetoForm()
    if request.method == 'GET':
        return render(request, 'gestao/adicionar-projeto.html', {'form_projeto': form})
    else: #POST
        
    
    return render(request, 'gestao/adicionar-projeto.html')