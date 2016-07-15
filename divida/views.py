from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import form_divida,\
    form_divida_descricao,\
    form_divida_consulta
from .models import comentario
from .models import divida as m_divida
from posto.models import credor
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .cnpj import Cnpj
from posto.cpf import CPF
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def multi_split(val_string):
    a = re.split("; |, |\*|\n|", val_string)
    lista = []
    for i in a:
        lista.append(i.strip())
    return ';'.join(lista)


@login_required
def divida(request):
    c_errors = ''
    if request.method == 'POST':
        data = request.POST.copy()
        try:
            data['valor'] = float(request.POST['valor'].replace('.', '').replace(',', '.'))
        except ValueError:
            data['valor'] = request.POST['valor']
        form = form_divida(data)
        form_desc = form_divida_descricao(request.POST)
        print form.is_valid()
        print form_desc.errors
        if form.is_valid() and form_desc.is_valid():
            cnpj_c = form.cleaned_data['ident_devedor']
            cpf = CPF(cnpj_c)
            if Cnpj().validate(cnpj_c) or cpf.isValid():
                print '2'
                new_divida = form.save(commit=False)
                new_divida_desc = form_desc.cleaned_data['descricao']
                new_divida.credor = credor.objects.get(email=request.user)
                new_divida.credor_cnpj = User.objects.get(id=request.user.id)
                new_divida.data_add = datetime.now()
                new_divida.descricao = new_divida_desc
                citados = ';'.join(
                    [
                        ' '.join([request.POST['citado'], request.POST['cpf']]),
                        ' '.join([request.POST['citado2'], request.POST['cpf2']])
                    ]
                )
                new_divida.citados = multi_split(val_string=citados)
                new_divida.save()
                return HttpResponseRedirect('/home')
            else:
                c_errors = 'cnpj'
                form = form_divida()
    else:
        form = form_divida()
    context = {
        'form': form,
        'credor':credor.objects.get(email=request.user),
        'c_errors': c_errors
    }
    return render(request, 'divida/divida.html', context)


@login_required
def consulta_divida(request):
    dividas = ''
    if request.method == 'POST':
        form = form_divida_consulta(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            dividas = m_divida.objects.filter(
                Q(nome_devedor__icontains=search) |
                Q(ident_devedor_cleaned__startswith=search.replace('/', '').replace('.', '').replace('-', '').strip()) |
                Q(citados__icontains=search)
            )
            if form.cleaned_data['inativos'] == 'True':
                dividas = dividas.filter(is_open=True)
    else:
        form = form_divida_consulta()

    paginator = Paginator(dividas, 20)

    page = request.GET.get('page')
    try:
        div_page = paginator.page(page)
    except PageNotAnInteger:
        div_page = paginator.page(1)
    except EmptyPage:
        div_page = paginator.page(paginator.num_pages)

    return render(
        request,
        'divida/consulta_divida.html',
        {
            'dividas': dividas,
            'form': form,
            'div_page': div_page,
            'paginator': paginator
        }
    )

@login_required
def divida_view(request, div_id):
    divida_var = m_divida.objects.get(id=div_id)
    if divida_var.citados is not None:
        divida_var.citados_as_list = divida_var.citados.split(';')
    else:
        divida_var.citados_as_list = ''
    if request.method == 'POST':
        form = form_divida_descricao(request.POST)
        if form.is_valid():
            com = form.cleaned_data['descricao']
            pago = form.cleaned_data['is_open']
            print pago
            c = comentario(
                divida=divida_var,
                credor=User.objects.get(id=request.user.id),
                coment=com,
                data_add=timezone.now()
            )
            if pago == 'True':
                print '1'
                divida_var.is_open = False
                divida_var.save()
                c.foi_paga = True
            else:
                c.foi_paga = False
            c.save()
    else:
        form = form_divida_descricao()
    comentarios = comentario.objects.filter(divida=divida_var).order_by('-data_add')
    context = {
        'divida_var': divida_var,
        'div_id': div_id,
        'comentarios': comentarios,
        'form': form
    }
    return render(request, 'divida/divida_detail.html', context)

