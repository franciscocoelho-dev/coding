from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto, Tarefa
from .forms import ProjetoForm, TarefaForm

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


def detalhar_projeto(request, id):
    projeto = get_object_or_404(Projeto, pk=id)
    tarefas = Tarefa.objects.filter(projeto_vinculado = projeto)
    return render(request, 'gestao/detalhes-projeto.html', {'projeto': projeto, 'tarefas': tarefas})

def cadastrar_tarefa(request, id):
    projeto = get_object_or_404(Projeto, pk=id)
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        form.cleaned_data['projeto_vinculado'] = projeto
        if form.is_valid():
            form.save()
    else:
        form = TarefaForm()
    return render(request, 'gestao/nova-tarefa.html', {'form': form})