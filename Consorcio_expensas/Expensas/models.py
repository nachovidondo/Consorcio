from django.db import models
from Administracion.models import Departamento,Edificio

# Create your models here.

 
class Expensas(models.Model):
    #montos generales
  
    pago_dpto = models.FloatField(verbose_name="Monto a pagar segun PH",blank = True, null = True)
    depto_ph = models.ForeignKey(Departamento,on_delete=models.CASCADE,blank = True, null = True)
    edificio_expensa= models.ForeignKey(Edificio,on_delete=models.CASCADE,verbose_name="Edificio",blank = True, null = True)
    # Monto Ingresos
    expensas_puras = models.FloatField(verbose_name="Expensas Puras",blank = True, null = True)
    total_ingresos = models.FloatField(verbose_name="Total ingresos",blank = True, null = True)
    deuda_totales = models.FloatField(verbose_name="Total Adeudado",blank = True, null = True, default=None)
    intereses_mora = models.FloatField(verbose_name="Intereses por Mora",blank = True, null = True)
    #Montos de Egresos
    materiales_limpieza = models.FloatField(verbose_name="materiales de limpieza",blank = True, null = True)
    servicios_luz= models.FloatField(verbose_name="servicios electricidad",blank = True, null = True)
    gastos_electricidad=models.FloatField(verbose_name="materiales y mano obra electricidad",blank = True, null = True)
    gastos_pintura=models.FloatField(verbose_name="materiales y mano obra pintura",blank = True, null = True)
    gastos_cerrajeria=models.FloatField(verbose_name=" materiales y mano de obra cerrajeria",blank = True, null = True)
    gastos_portero_electrico=models.FloatField(verbose_name="service portero electrico",blank = True, null = True)
    gastos_bomba_agua=models.FloatField(verbose_name="service bombas de agua",blank = True, null = True)
    gastos_matafuegos=models.FloatField(verbose_name=" recarga matafuegos",blank = True, null = True)
    gastos_accesorios=models.FloatField(verbose_name=" gastos accesorios",blank = True, null = True)
    vacaciones_encargado =models.FloatField(verbose_name=" vacaciones encargado",blank = True, null = True)
    reemplazo_encargado=models.FloatField(verbose_name=" reemplazo encargado",blank = True, null = True)
    sueldo_administrador = models.FloatField(verbose_name="Sueldo Administrador",blank = True, null = True)
    ascensores = models.FloatField(verbose_name="Gasto Ascensores",blank = True, null = True)
    aportes_encargado_limpieza = models.FloatField(verbose_name="Aportes Encargado Limpieza",blank = True, null = True)
    sueldo_encargado_limpieza = models.FloatField(verbose_name="Sueldo Encargado Limpieza",blank = True, null = True)
    seguro_edificio = models.FloatField(verbose_name="Seguro Edificio",blank = True, null = True)
    sueldo_anual_complementario = models.FloatField(verbose_name="Sueldo Anual Complementario",blank = True, null = True)
    total_gastos = models.FloatField(verbose_name="Total de Gastos (Egreso) ",blank = True, null = True, default=0)
    porcentaje_correspondiente_dpto = models.FloatField(verbose_name="Porcentaje Correspondiente Departamento",blank = True, null = True)
    
    

    
    
    class Meta:
        verbose_name = "Expensas"
        verbose_name_plural = "Expensas"
        
    def __str__(self):
        return self.expensa
        