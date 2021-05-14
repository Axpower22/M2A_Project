"""M2A URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from M2A_app.views import msg_test, msg_test2, datahora, login, cadastro_usuario, cadastro_empresa, lista_diagnostico,\
    lista_empresa, lista_grupo, lista_usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('msg_test/', msg_test),
    path('msg_test2/', msg_test2),
    path('data/', datahora),
    path('login/', login),
    path('cadastro_usuario/', cadastro_usuario),
    path('cadastro_empresa/', cadastro_empresa),
    path('lista_diagnosticos/', lista_diagnostico),
    path('lista_empresa/', lista_empresa),
    path('lista_grupo/', lista_grupo),
    path('lista_usuario/', lista_usuario),


]