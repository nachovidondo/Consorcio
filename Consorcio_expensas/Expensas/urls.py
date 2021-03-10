from django.urls import path
from .views import ExpensaCreate,ExpensasListView

urlpatterns = [

    path('crear_expensa/',ExpensaCreate.as_view(),name = "crear_expensa"),
    path('listar_expensa/',ExpensasListView.as_view(),name ="listar_expensa")
    
]