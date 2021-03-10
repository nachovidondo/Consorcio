from django.contrib import admin
from .models import Departamento, Edificio
# Register your models here.
class DepartamentoAdmin(admin.ModelAdmin):
    list_display=['ph','edificio_nombre','porcentaje_correspondiente']
    search_fields=['ph']
  
admin.site.register(Edificio)
admin.site.register(Departamento,DepartamentoAdmin)    
