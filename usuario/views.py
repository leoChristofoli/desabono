from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime
from .forms import form_user
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from posto.models import credor
from divida.models import divida as divida_model
from django.contrib.auth.decorators import login_required, user_passes_test


def login_view(request):
    if request.method == 'POST':
        form = form_user(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['password']
            user = authenticate(username=email, password=pwd)
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
        dividas_count = divida_model.objects.filter(credor_cnpj=user).count()
        dividas_enc_count = divida_model.objects.filter(credor_cnpj=user).filter(is_open=False).count()
        dividas_abertas_count = divida_model.objects.filter(credor_cnpj=user).filter(is_open=True).count()
        context = {
            'user_profile': user_profile,
            'dividas_enc_count': dividas_enc_count,
            'dividas_abertas_count': dividas_abertas_count,
            'dividas_count': dividas_count
        }
    else:
        context = {}
    template = 'usuario/detail.html'
    return render(request, template, context)

