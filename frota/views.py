from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views import generic
from . import models

def index(request):
    all_clientes = models.Cliente.objects.all()
    return render(request, 'index.html', { 'clientes': all_clientes})

class ClienteListView(generic.ListView):
    template_name = 'cliente_list.html'
    model = models.Cliente
