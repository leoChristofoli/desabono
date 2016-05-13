from django.forms import ModelForm
from models import credor
from django import forms

class form_credor(ModelForm):
    class Meta:
        model = credor
        fields = ['nome', 'sobrenome', 'cnpj', 'endereco']


class form_credor_user(forms.Form):
        email = forms.EmailField(
            max_length=200
        )
        password = forms.CharField(
            min_length=6,
            max_length=100,
            widget=forms.PasswordInput
        )
        password_check = forms.CharField(
            min_length=6,
            max_length=100,
            widget=forms.PasswordInput
        )
