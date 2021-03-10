from Expensas.forms import ExpensasForm
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Expensas

# Create your views here.

class ExpensaCreate(CreateView):
    model = Expensas
    form_class = ExpensasForm
    template_name = "create_expensa.html"
    success_url ='index'
    
    
    