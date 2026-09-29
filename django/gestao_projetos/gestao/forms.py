from django import forms
from django.forms import ModelForm
from .models import Projeto

class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'
        exclude = ('status',)

        widgets = {
            'nome' : forms.TextInput(attrs={
                'placeholder': 'Informe o nome do projeto'
            }),

            'data_inicio': forms.DateInput(attrs={
                'type': 'date'
            })
        }

    def clean_nome(self):
        valor_nome = self.cleaned_data.get('nome', '').strip()
        if len(valor_nome) < 20:
            self.add_error('nome', 'O nome deve ter no mínimo 20 caracteres')
        return valor_nome
