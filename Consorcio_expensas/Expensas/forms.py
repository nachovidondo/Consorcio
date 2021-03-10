from django import forms
from .models import Expensas

class ExpensasForm(forms.ModelForm):
    class Meta:
        model = Expensas
        fields ='__all__'
      