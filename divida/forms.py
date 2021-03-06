# coding=utf-8
from django.forms import ModelForm
from django import forms
from models import divida
from datetime import datetime, date


class form_divida(ModelForm):
    class Meta:
        model = divida
        fields = ['valor',
                  'nome_devedor',
                  'ident_devedor',
                  'vencimento',
                  'tipo_divida']

    def clean_vencimento(self):
        date = self.cleaned_data['vencimento']
        if date > date.today():
            raise forms.ValidationError("Apenas datas passadas")
        return date


BOOL_CHOICES = (
    ('True', 'Sim'),
    ('False', 'Não')
)


class form_divida_descricao(forms.Form):
    descricao = forms.CharField(min_length=0, max_length=8000)
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
