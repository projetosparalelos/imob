__author__ = 'gpzim98'
from django import forms
from funcionarios.models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        exclude = ['endereco',]
