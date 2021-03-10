from django.urls import path
from .views import ExpensasCreate,ExpensasListView,ExpensasUpdateView,ExpensasDetailView

urlpatterns = [

    path('crear_expensa/',ExpensasCreate.as_view(),name = "crear_expensa"),
    path('listar_expensa/',ExpensasListView.as_view(),name ="listar_expensa"),
    path('editar_expensa/<int:pk>/',ExpensasUpdateView.as_view(),name = 'editar_expensa'),
    path('detalle_expensa',ExpensasDetailView.as_view(),name ="detalle_expensa")
    
]