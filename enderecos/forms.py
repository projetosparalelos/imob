__author__ = 'gpzim98'
from django import forms
from enderecos.models import Endereco, Bairro, Cidade


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        exclude = ['*']


class BairroForm(forms.ModelForm):
    class Meta:
        model = Bairro
        fields = ['nome', 'cidade']
        readonly = ('codigo',)
        exclude = ['*']


class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        exclude = ['*']
