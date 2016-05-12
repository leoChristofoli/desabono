from django.forms import ModelForm
from models import credor
from django import forms
from django.contrib.auth.models import User

class form_credor(ModelForm):
    class Meta:
        model = credor
        fields = ['nome', 'cnpj', 'endereco']


class form_credor_user(forms.Form):
        email = forms.EmailField(
            max_length=200
        )
        password = forms.CharField(
            max_length=100,
            widget=forms.PasswordInput
        )
        password_check = forms.CharField(
            min_length=6,
            max_length=100,
            widget=forms.PasswordInput
        )
