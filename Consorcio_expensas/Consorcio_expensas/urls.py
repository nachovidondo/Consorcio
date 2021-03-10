from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView 
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('admin/', admin.site.urls),
     path('login/',LoginView.as_view(template_name ="login.html"),name ="login"),
    path('logout/',LogoutView.as_view(template_name ="login.html"), name="logout"),
    path('',login_required(include('Administracion.urls'))),
    path('expensa/',login_required(include('Expensas.urls'))),
]
