from django import forms
from .models import Departamento

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields =['ph','deuda_mes','total_deuda']
        labels = {
            'ph' : 'Ph del departamento',
            'deuda_mes' : 'Deuda del mes',
            'total_deuda' : 'Total Deuda',
        }
    
