from django.shortcuts import render
from django.http import HttpResponse
import datetime

def msg_test(request):
    m = "Bem vindo Teste"
    return HttpResponse(m)

def msg_test2(request):
    return HttpResponse('Bem Vindo')

def datahora(request):
    now = datetime.datetime.now()
    html = "<html><body>is %s.<body><html>" %now
    return HttpResponse(html)

def login(request):
    return render(request, 'M2A_app/login.html')

def cadastro_usuario(request):
    return render(request, 'M2A_app/cadastro_usuario.html')
# Create your views here.