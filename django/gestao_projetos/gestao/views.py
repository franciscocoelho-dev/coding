from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listar_projetos)
    else:
        # request.method == 'GET'
        form = ProjetoForm()
    return render(request, 'gestao/adicionar-projeto.html', {'form': form})



    