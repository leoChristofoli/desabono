from django.shortcuts import render
from .forms import form_divida
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import divida


def divida(request):
    if request.method == 'POST':
        form = form_divida(request.POST)
        if form.is_valid():
            new_divida = form.save(commit=False)
            new_divida.data_add = datetime.now()
            new_divida.save()
            return HttpResponseRedirect('/')
    else:
        form = form_divida()
    return render(request, 'divida/divida.html', {'form': form})
