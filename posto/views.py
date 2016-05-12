from django.shortcuts import render
from .forms import form_credor, form_credor_user
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import credor
from django.contrib.auth.models import User


def index(request):
    context = {}
    template = 'posto/index.html'
    return render(request, template, context)


def cadastro(request):
    if request.method == 'POST':
        form = form_credor(request.POST)
        form_user = form_credor_user(request.POST)

        if form.is_valid() and form_user.is_valid():

            email = form_user.cleaned_data['email']
            pwd = form_user.cleaned_data['password']
            pwd_check = form_user.cleaned_data['password_check']
            if pwd == pwd_check:
                user = User.objects.create_user(username=email, password=pwd)
                user.save()

            new_user = form.save(commit=False)
            new_user.data_add = datetime.now()
            new_user.ip_user = '111.111.111.1'
            new_user.save()
            return HttpResponseRedirect('/')
    else:
        form = form_credor()
        form_user = form_credor_user()
    return render(request,
                  'posto/cadastro.html',
                  {
                      'form': form,
                      'form_user': form_user
                  })


def credores(request):
    usuarios = credor.objects.all()
    return render(request, 'posto/users.html', {'usuarios': usuarios})
