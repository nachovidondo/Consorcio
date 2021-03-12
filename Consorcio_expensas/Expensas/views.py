from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from Expensas.forms import ExpensasForm
from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,View
from django.urls import reverse_lazy
from .models import Expensas
from django.http import HttpResponse
from django.template.loader import get_template
from django.http.response import HttpResponseRedirect
from xhtml2pdf import pisa
from Consorcio_expensas.utils import render_to_pdf 


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


    
class ExpensasPDFDetail(View):
    
    def get(self, request,*args,**kwargs):
        template = get_template('expensa_pdf.html')
        context = {}
        context['expensas'] = Expensas.objects.all()
        html = template.render(context)
        pdf = render_to_pdf('expensa_pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "expensa_pdf_%s.pdf" %("1")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")