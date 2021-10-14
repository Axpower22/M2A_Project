from django.shortcuts import render, redirect
from M2A_app.models import *
from M2A_app.forms import *


def login(request):
    return render(request, 'M2A_app/login.html')


def cadastro_usuario(request):
    return render(request, 'M2A_app/cadastro_usuario.html')


def cadastro_empresa(request):
    if request.method == 'GET':
        ufs = UF.objects.all()
        return render(request, 'M2A_app/cadastro_empresa.html', {'ufs': ufs})
    elif request.method == 'POST':
        nova_empresa = EmpresaForm(request.POST)

        if nova_empresa.is_valid():
            nova_empresa.save()

        return redirect('/lista_empresa')


def lista_diagnostico(request):
    diagnosticos = Diagnostico.objects.all()
    return render(request, 'M2A_app/lista_diagnostico.html', {'diagnosticos': diagnosticos})


def lista_empresa(request):
    empresas = Empresa.objects.all()
    return render(request, 'M2A_app/lista_empresas.html', {'empresas': empresas})


def lista_grupo(request):
    grupos = Grupo.objects.all()
    return render(request, 'M2A_app/lista_grupo.html', {'grupos': grupos})


def lista_usuario(request):
    usuarios = Usuario.objects.all()
    return render(request, 'M2A_app/lista_usuario.html', {'usuarios': usuarios})


def lista_respostas(request):
    return render(request, 'M2A_app/lista_respostas.html')


def dados_usuario(request):
    return render(request, 'M2A_app/dados_usuario.html')


def graficos(request):
    return render(request, 'M2A_app/graficos.html')


def registro_grupo(request):
    return render(request, 'M2A_app/registro_grupo.html')


def cadastro_diagnostico(request):
    return render(request, 'M2A_app/cadastro_diagnostico.html')


def cadastro_respostas(request):
    return render(request, 'M2A_app/cadastro_respostas.html')


def cadastro_perguntas(request):
    return render(request, 'M2A_app/cadastro_perguntas.html')