from django.urls import path
from .views import ExpensaCreate

urlpatterns = [

    path('create_expensa/',ExpensaCreate.as_view(),name = "create_expensa"),
    
]