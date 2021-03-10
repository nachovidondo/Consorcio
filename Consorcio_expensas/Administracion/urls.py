from django.urls import path
from .views import DepartamentoUpdateView, EdificioListView,EdificioDetalleListView,Expensa
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('index/',login_required(EdificioListView.as_view()),name ="index"),
    path('detalle_edificio/',login_required(EdificioDetalleListView.as_view()),name ="detalle_edificio"),
    path('editar_dpto/<int:pk>/',login_required(DepartamentoUpdateView.as_view()), name= "editar_dpto"),
    path('expensa/',login_required(Expensa.as_view()),name = "expensa"),
    
]