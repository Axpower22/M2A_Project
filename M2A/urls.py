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
from M2A_app.views import login, cadastro_usuario, cadastro_empresa, lista_diagnostico,\
    lista_empresa, lista_grupo, lista_usuario, lista_respostas, dados_usuario, graficos, registro_grupo,\
    cadastro_diagnostico, cadastro_respostas, cadastro_perguntas


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('cadastro_usuario/', cadastro_usuario),
    path('cadastro_empresa/', cadastro_empresa),
    path('lista_diagnosticos/', lista_diagnostico),
    path('lista_empresa/', lista_empresa),
    path('lista_grupo/', lista_grupo),
    path('lista_usuario/', lista_usuario),
    path('lista_respostas/', lista_respostas),
    path('dados_usuario/', dados_usuario),
    path('graficos/', graficos),
    path('registro_grupo/', registro_grupo),
    path('cadastro_diagnostico/', cadastro_diagnostico),
    path('cadastro_respostas/', cadastro_respostas),
    path('cadastro_perguntas/', cadastro_perguntas),
]