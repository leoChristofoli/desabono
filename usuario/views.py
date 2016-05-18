from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime
from .forms import form_user
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from posto.models import credor


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


def user_view(request, user_id):
    user = User.objects.get(id=user_id)
    user_profile = credor.objects.get(email=user)
    context = {
        'user_profile': user_profile
    }
    template = 'usuario/detail.html'
    return render(request, template, context)

