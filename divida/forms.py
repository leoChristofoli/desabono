from django.forms import ModelForm
from django import forms
from models import divida


class form_divida(ModelForm):
    class Meta:
        model = divida
        fields = ['valor',
                  'vencimento',
                  'citado',
                  'tipo_divida',
                  'termos']


class form_divida_descricao(forms.Form):
    descricao = forms.CharField(max_length='8000')
