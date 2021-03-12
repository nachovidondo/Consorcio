from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.views.generic.base import View
from django.views.generic.edit import UpdateView
from .models import Departamento, Edificio
from django.views.generic import ListView, CreateView,DetailView,UpdateView
from django.db.models import Q
from .forms import DepartamentoForm
from django.urls import reverse_lazy
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
# Create your views here.


class EdificioListView(ListView):
    model = Edificio
    template_name = 'index.html'
    context_object_name ='edificios'
    
class EdificioDetalleListView(ListView):
    model = Departamento
    template_name = 'detalle_edificio.html'
    context_object_name = 'Departamento'
    
    def get_queryset(self):
        qs=Departamento.objects.all()
        edificio_id = self.request.GET.get('lang')
        if edificio_id:
            qs = qs.filter(edificio_nombre__id = edificio_id)
            
        return qs    

class DepartamentoUpdateView(UpdateView):
    model = Departamento
    template_name = 'editar_dpto.html'
    form_class = DepartamentoForm
    success_url = reverse_lazy('detalle_edificio')


    
        