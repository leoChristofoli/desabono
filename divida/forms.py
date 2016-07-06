# coding=utf-8
from django.forms import ModelForm
from django import forms
from models import divida


class form_divida(ModelForm):
    class Meta:
        model = divida
        fields = ['valor',
                  'nome_devedor',
                  'ident_devedor',
                  'vencimento',
                  'tipo_divida']

    def clean_valor(self):
        valor = self.cleaned_data['valor']
        valor = valor.replace(',', '')
        return valor


BOOL_CHOICES = (
    ('True', 'Sim'),
    ('False', 'Não')
)


class form_divida_descricao(forms.Form):
    descricao = forms.CharField(min_length=4, max_length=8000)
    is_open = forms.ChoiceField(
        required=False,
        initial=False,
        widget=forms.RadioSelect,
        choices=BOOL_CHOICES
    )


class form_divida_consulta(forms.Form):
    search = forms.CharField(min_length=2, max_length=2000)
    inativos = forms.ChoiceField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput,
        choices=BOOL_CHOICES
    )
