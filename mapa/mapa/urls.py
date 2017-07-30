"""mapa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login
from mapa_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^listar', views.listar_pontos, name='listar'),
    url(r'^fococalor', views.fococalor, name='fococalor'),
    url(r'^chamados', views.chamados, name='chamados'),
    url(r'^relatorio_data', views.relatorio_data, name='relatorio_data'),
    url(r'^login/', views.logar, name='login'),
    url(r'^login_app/', views.login_app, name='login_app'),
    url(r'^logout/', views.deslogar, name='logout'),
    url(r'^addchamado/', views.abrir_chamado, name='addchamado'),
    url(r'^cad-abrigo/', views.cad_abrigo, name='cad-abrigo'),
    url(r'^det-abrigo/', views.detalhe_abrigo, name='det-abrigo'),
    url(r'^cota-atual/', views.cota_atual, name='cota-atual'),
    url(r'^$', views.listar_pontos, name='index'),

]

