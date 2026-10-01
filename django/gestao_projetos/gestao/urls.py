from django.urls import path
from .views import gestao_home, listar_projetos, adicionar_projetos, detalhar_projeto

urlpatterns = [
    path('', gestao_home, name = 'gestao-home'),
    path('projetos/', listar_projetos, name = 'listar-projetos'),
    
    path('projetos/adicionar/', adicionar_projetos, name='adicionar-projeto'),

    path('projetos/<int:id>/detalhar/', detalhar_projeto, name='detalhar-projeto')
]


