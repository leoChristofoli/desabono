from django.forms import ModelForm
from models import credor

class form_credor(ModelForm):
    class Meta:
        model = credor
        fields = ['nome', 'cnpj', 'endereco', 'email']

