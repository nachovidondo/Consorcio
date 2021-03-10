from django.db import models

# Create your models here.
class Edificio(models.Model):
    nombre = models.CharField(max_length = 50 ,verbose_name="Edificio")
    class Meta:
        verbose_name ="Edificio"
        verbose_name_plural = "Edificios"
    def __str__(self):
        return self.nombre
class Departamento(models.Model):
    ph = models.CharField(max_length=50, verbose_name="Departamento PH")
    porcentaje_correspondiente = models.FloatField(verbose_name="Porcentaje Correspondiente del Total", default=1)
    deuda_mes = models.FloatField(verbose_name="Deuda del Mes")
    total_deuda= models.FloatField(verbose_name="Deuda Total")
    edificio_nombre= models.ForeignKey(Edificio,verbose_name="Edificio",on_delete=models.CASCADE,default = None)
    class Meta:
        verbose_name ="Departamento"
        verbose_name_plural ="Departamentos"
    
    def __str__(self):
        return self.ph
    
    
 