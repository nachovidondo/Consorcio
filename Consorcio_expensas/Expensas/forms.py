from django import forms
from .models import Expensas

class ExpensasForm(forms.ModelForm):
    class Meta:
        model = Expensas
        fields ='__all__'
        labels = {
            'depto_ph': 'Ph del Departamento',
            'edificio_expensa':'Edificio',
            'expensas_puras': 'Expensas Puras',
            'total_ingresos':'Total de Ingresos',
            'deuda_totales':'Deuda Total del Edificio',
            'intereses_mora':'Intereses por mora',
            'materiales_limpieza':'Materiales de limpieza',
            'servicios_luz':'Servicios de luz',
            'gastos_electricidad':'Gastos de electricidad',
            'gastos_cerrajeria':'Gastos de cerrajeria',
            'gastos_portero_electrico':'Gastos portero electrico',
            'gastos_bomba_agua':'Gastos bomba de agua',
            'gastos_matafuegos':'Gastos de matafuego',
            'gastos_accesorios':'Gastos accesorios',
            'vacaciones_encargado':'Vacaciones encargado',
            'reemplazo_encargado':'Reemplazo de encargado',
            'sueldo_administrador':'Sueldo del Administrador',
            'ascensores':'Ascensores',
            'aportes_encargado_limpieza':'Aportes encargado de limpieza',
            'sueldo_encargado_limpieza':'Sueldo encargado de limpieza',
            'seguro_edificio':'Seguro edificio',
            'sueldo_anual_complementario':'Sueldo anual complementario',
            'total_gastos':'Total de gastos',
            'porcentaje_correspondiente_dpto':'Porcentaje correspondiente PH'
            }
            
     