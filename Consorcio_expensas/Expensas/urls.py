from django.urls import path
from .views import ExpensasCreate,ExpensasListView,ExpensasUpdateView,ExpensasDetailView,ExpensasPDFDetail
from django.contrib.auth.decorators import login_required
urlpatterns = [

    path('crear_expensa/',login_required(ExpensasCreate.as_view()),name = "crear_expensa"),
    path('listar_expensa/',login_required(ExpensasListView.as_view()),name ="listar_expensa"),
    path('editar_expensa/<int:pk>/',login_required(ExpensasUpdateView.as_view()),name = 'editar_expensa'),
    path('detalle_expensa/<int:pk>/',login_required(ExpensasDetailView.as_view()),name ="detalle_expensa"),
    path('expensa_pdf/<int:pk>/',login_required(ExpensasPDFDetail.as_view()),name ="expensa_pdf"),
   
    
    
]