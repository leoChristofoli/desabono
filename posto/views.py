from django.shortcuts import render
from .forms import form_credor
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import credor


def index(request):
    context = {}
    template = 'posto/index.html'
    return render(request, template, context)


def cadastro(request):
    if request.method == 'POST':
        form = form_credor(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.data_add = datetime.now()
            new_user.ip_user = '111.111.111.1'
            new_user.save()
            return HttpResponseRedirect('/')
    else:
        form = form_credor()
    return render(request, 'posto/cadastro.html', {'form': form})


def credores(request):
    usuarios = credor.objects.all()
    return render(request, 'posto/users.html', {'usuarios': usuarios})
