from django.shortcuts import render
from .forms import form_divida, form_divida_descricao
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import divida as m_divida
from .models import comentario
from django.contrib.auth.models import User


def divida(request):
    if request.method == 'POST':
        form = form_divida(request.POST)
        form_desc = form_divida_descricao(request.POST)
        if form.is_valid() and form_desc.is_valid():
            new_divida = form.save(commit=False)
            new_divida_desc = form_desc.cleaned_data['descricao']
            new_divida.credor_cnpj = User.objects.get(id=request.user.id)
            new_divida.data_add = datetime.now()
            new_divida.descricao = new_divida_desc
            new_divida.save()
            return HttpResponseRedirect('/')
    else:
        form = form_divida()
    return render(request, 'divida/divida.html', {'form': form})


def consulta_divida(request):
    dividas = m_divida.objects.all()
    return render(request, 'divida/consulta_divida.html', {'dividas': dividas})


def divida_view(request, div_id):
    divida_var = m_divida.objects.get(id=div_id)
    comentarios = comentario.objects.filter(divida=divida_var)
    context = {
        'divida_var': divida_var,
        'comentarios': comentarios
    }
    return render(request, 'divida/divida_detail.html', context)

