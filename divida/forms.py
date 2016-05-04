from django.forms import ModelForm
from models import divida

class form_divida(ModelForm):
    class Meta:
        model = divida
        fields = ['credor_cnpj',
                  'valor',
                  'vencimento',
                  'descricao',
                  'citado',
                  'tipo_divida',
                  'termos']

