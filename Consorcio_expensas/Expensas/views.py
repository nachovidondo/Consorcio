from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from Expensas.forms import ExpensasForm
from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView
from django.urls import reverse_lazy
from .models import Expensas

# Create your views here.

class ExpensasCreate(CreateView):
    model = Expensas
    form_class = ExpensasForm
    template_name = "crear_expensa.html"
    success_url = reverse_lazy('listar_expensa')
    
    
class ExpensasListView(ListView):
    model = Expensas
    template_name ="listar_expensa.html"
    context_object_name = 'expensas'
    
class ExpensasUpdateView(UpdateView):
    model = Expensas
    form_class = ExpensasForm
    template_name ="editar_expensa.html"
    success_url = reverse_lazy('listar_expensa')

class ExpensasDetailView(DetailView):
    model = Expensas
    template_name ="detalle_expensa.html"
    context_object_name ="expensas"
