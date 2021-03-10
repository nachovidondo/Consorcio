from django.urls import path
from .views import DepartamentoUpdateView, EdificioListView,EdificioDetalleListView,Expensa

urlpatterns = [
    path('index/',EdificioListView.as_view(),name ="index"),
    path('detalle_edificio/',EdificioDetalleListView.as_view(),name ="detalle_edificio"),
    path('editar_dpto/<int:pk>/',DepartamentoUpdateView.as_view(), name= "editar_dpto"),
    path('expensa/',Expensa.as_view(),name = "expensa"),
    
]