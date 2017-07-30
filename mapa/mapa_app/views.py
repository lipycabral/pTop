# -*- coding: utf-8 -*-
from datetime import datetime, time
import hashlib
import urllib.parse
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import simplejson
from mapa_app.models import *
import urllib.request
import json
# from django.utils import simplejson

# Create your views here.
@login_required
def listar_pontos(request):
    pontos = Local.objects.all()
    email = hashlib.md5(request.user.email.encode('utf-8')).hexdigest()
    req = urllib.request.urlopen('http://iot-acre.mybluemix.net/api/acre4')
    jsonstr = req.read()
    json_obj = json.loads(jsonstr)
    ultimo = json_obj[-1]
    return render(request, 'lista_pontos.html', locals())


@login_required
def chamados(request):
    pontos = Local.objects.all()
    req = urllib.request.urlopen('http://iot-acre.mybluemix.net/api/acre4')
    jsonstr = req.read()
    json_obj = json.loads(jsonstr)
    ultimo = json_obj[-1]
    return render(request, 'chamados.html', locals())


@login_required
def relatorio_data(request):
    email = hashlib.md5(request.user.email.encode('utf-8')).hexdigest()
    di = datetime.strptime(request.GET.get('datainicial'), '%Y-%m-%d').date()  # 'dd-mm-yyyy'
    datafinal = datetime.strptime(request.GET.get('datafinal'), '%Y-%m-%d').date()
    df = datetime.combine(datafinal, time.max)
    pontos = Local.objects.filter(dt_atualiza__gte=di, dt_atualiza__lte=df, )
    return render(request, 'chamados_data.html', locals())


def logar(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(username=usuario, password=senha)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['usuario'] = usuario
                if request.GET.get('next'):
                    return HttpResponseRedirect(request.GET.get('next'))
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.error(request, 'O usuário não está ativo')
        else:
            messages.error(request, 'Por favor, insira um usuário e senha corretos.')
    else:
        logout(request)
    return TemplateResponse(request, 'login.html', locals())


def deslogar(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


# view cadastro via app
def abrir_chamado(request):
    codusuario = request.GET.get('codusuario')
    mensagem = request.GET.get('mensagem')
    tipo = request.GET.get('titulo')
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    chamado = Local(codusuario_id=codusuario, titulo=tipo, denuncia=mensagem, latitude=latitude, longitude=longitude)
    chamado.save()

    mensagem = {
        'mensagem': u'Gravado com sucesso %s' % chamado.titulo,
    }
    # data = simplejson.dumps(mensagem)
    return HttpResponse(u'Gravado com sucesso %s' % chamado.titulo)


@login_required
def fococalor(request):
    foco = Local.objects.all()
    email = hashlib.md5(request.user.email.encode('utf-8')).hexdigest()
    return render(request, 'mapa_calor.html', locals())


@csrf_exempt
def login_app(request):
    # if request.method == 'POST':
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    user = authenticate(username=usuario, password=senha)
    if user is not None:
        if user.is_active:
            return HttpResponse(u'Logado com sucesso %s' % user.first_name)
        else:
            return HttpResponse(u'O usuário não está ativo')
    else:
        return HttpResponse(u'Por favor, insira um usuário e senha corretos.')


@login_required
def cad_abrigo(request):
    abrigos = Abrigo.objects.all()
    email = hashlib.md5(request.user.email.encode('utf-8')).hexdigest()
    return render(request, 'cad_abrigos.html', locals())


@login_required
def detalhe_abrigo(request):
    codabrigo = request.GET.get('cod')
    abrigo = Abrigo.objects.filter(id=codabrigo)
    desabrigados = Abrirelaciona.objects.filter(codabrigo__pk=request.GET['cod'])
    quantidade = desabrigados.count()
    return render(request, 'det-abrigos.html', locals())

@login_required
def cota_atual(request):
    return render(request, 'base.json', locals())