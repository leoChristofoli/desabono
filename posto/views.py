from django.shortcuts import render
from .forms import form_credor, form_credor_user
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import credor
from divida.models import divida as divida_model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .cnpj import Cnpj
from .cpf import CPF
from django.db import IntegrityError



def get_ip(request):
    try:
        x_forwarded = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded:
            ip = x_forwarded.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""
    return ip


def index(request):
    dividas_count = divida_model.objects.count()
    context = {
        'dividas_count': dividas_count
    }
    print(request.user.is_authenticated)
    if request.user.is_authenticated():
        template = 'posto/index_log.html'
    else:
        template = 'posto/index.html'
    return render(request, template, context)


def cadastro(request):
    c_errors = ''
    if request.method == 'POST':
        form = form_credor(request.POST)
        form_user = form_credor_user(request.POST)
        print(form.is_valid())
        if form.is_valid() and form_user.is_valid():
            cnpj_c = form.cleaned_data['cnpj'].replace('/', '').replace('-', '').replace('.', '')
            cpf = CPF(cnpj_c)
            if Cnpj().validate(cnpj_c) or cpf.isValid():
                email = form_user.cleaned_data['email']
                pwd = form_user.cleaned_data['password']
                pwd_check = form_user.cleaned_data['password_check']
                nome = form.cleaned_data['nome']
                snome = form.cleaned_data['sobrenome']
                new_user = form.save(commit=False)
                if pwd == pwd_check:
                    try:
                        user = User.objects.create_user(
                            username=email,
                            password=pwd,
                            first_name=nome,
                            last_name=snome
                        )
                        user.save()
                        new_user.email = user
                    except IntegrityError as e:
                        c_errors = 'email'
                        return render(request,'posto/cadastro.html', {
                            'form': form,
                            'form_user': form_user,
                            'c_errors': c_errors
                        })
                new_user.cnpj = cnpj_c
                new_user.data_add = datetime.now()
                new_user.ip_user = get_ip(request)
                new_user.save()
                logout(request)
                user = authenticate(username=email, password=pwd)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect('/logon_fail')
                return HttpResponseRedirect('/')
            else:
                c_errors = 'cnpj'
                form = form_credor()
                form_user = form_credor_user()
    else:
        form = form_credor()
        form_user = form_credor_user()
    return render(request,
                  'posto/cadastro.html',
                  {
                      'form': form,
                      'form_user': form_user,
                      'c_errors': c_errors
                  })


def credores(request):
    usuarios = credor.objects.all()
    return render(request, 'posto/users.html', {'usuarios': usuarios})
