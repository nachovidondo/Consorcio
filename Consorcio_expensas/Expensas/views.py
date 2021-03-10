from Expensas.forms import ExpensasForm
from django.shortcuts import render
from django.views.generic import CreateView,ListView
from .models import Expensas
from django.urls import reverse_lazy

# Create your views here.

class ExpensaCreate(CreateView):
    model = Expensas
    form_class = ExpensasForm
    template_name = "crear_expensa.html"
    success_url = reverse_lazy('listar_expensa')
    
    
class ExpensasListView(ListView):
    model = Expensas
    template_name ="listar_expensa.html"
    context_object_name = 'expensas'