# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime
from .forms import form_user, form_forgot
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from posto.models import credor
from divida.models import divida as divida_model
from django.contrib.auth.decorators import login_required, user_passes_test
import string
import random
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def login_view(request):
    if request.method == 'POST':
        form = form_user(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['password']
            user = authenticate(username=email.strip(), password=pwd)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(request.POST.get('next'))
                else:
                    form_errors = form.errors
            else:
                form_errors = form.errors
        else:
            form_errors = form.errors
    else:
        form = form_user()
        form_errors = ''
    return render(
        request,
        'usuario/logon.html',
        {
            'form': form,
            'form_errors': form_errors
        }
        )


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def user_check(request, user_id):
    if user_id == request.user.id:
        return True
    else:
        return False


@login_required
def user_view(request, user_id):
    if int(request.user.id) == int(user_id):
        user = User.objects.get(id=user_id)
        user_profile = credor.objects.get(email=user)
        user_credor = credor.objects.get(email=request.user)
        dividas = divida_model.objects.filter(credor_cnpj=user).order_by('data_add')
        dividas_count = divida_model.objects.filter(credor_cnpj=user).count()
        dividas_enc_count = divida_model.objects.filter(credor_cnpj=user).filter(is_open=False).count()
        dividas_abertas_count = divida_model.objects.filter(credor_cnpj=user).filter(is_open=True).count()

        paginator = Paginator(dividas, 20)

        page = request.GET.get('page')
        try:
            div_page = paginator.page(page)
        except PageNotAnInteger:
            div_page = paginator.page(1)
        except EmptyPage:
            div_page = paginator.page(paginator.num_pages)

        context = {
            'user_profile': user_profile,
            'credor': user_credor,
            'div_page': div_page,
            'dividas_enc_count': dividas_enc_count,
            'dividas_abertas_count': dividas_abertas_count,
            'dividas_count': dividas_count
        }
    else:
        context = {}
    template = 'usuario/detail.html'
    return render(request, template, context)


def pass_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def forgot_pass_view(request):
    if request.method == 'POST':
        form = form_forgot(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(username=email)
            print(user)
            senha = pass_generator()
            user.set_password(senha)
            send_mail('Senha desabono', 'Sua nova senha do desabono.com é {pwd}'.format(pwd=senha), 'desabonotm@gmail.com',
                      [user.username, ], fail_silently=False)
            user.save()
    else:
        form = form_forgot()
    context = {
        'form': form
    }
    template = 'usuario/forgot_pwd.html'
    return render(request, template, context)

