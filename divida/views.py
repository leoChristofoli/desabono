from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import form_divida, form_divida_descricao
from .models import comentario
from .models import divida as m_divida


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
    if request.method == 'POST':
        form = form_divida_descricao(request.POST)
        print form.is_valid()
        if form.is_valid():
            com = form.cleaned_data['descricao']
            print com
            comentario.objects.create(
                divida=divida_var,
                credor=User.objects.get(id=request.user.id),
                coment=com,
                data_add=timezone.now()
            )
    else:
        form = form_divida_descricao()
    comentarios = comentario.objects.filter(divida=divida_var)
    context = {
        'divida_var': divida_var,
        'div_id': div_id,
        'comentarios': comentarios
    }
    return render(request, 'divida/divida_detail.html', context)

