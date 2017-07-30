from django.contrib import admin
from mapa_app.models import *

# Register your models here.
class Localadmin(admin.ModelAdmin):
    list_display = ['titulo']
class Usuarioadmin(admin.ModelAdmin):
    list_display = ['nome', 'id']
class Mensagemadmin(admin.ModelAdmin):
    list_display = ['datamensagem', 'mensagem', 'resposta']
    list_filter = ['resposta',]
class Localadmin(admin.ModelAdmin):
        list_display = ['titulo']


class CadastroAdmin(admin.ModelAdmin):
    list_display = ['nome']
admin.site.register(Local, Localadmin)
admin.site.register(Cadastro, CadastroAdmin)
# admin.site.register(Usuario, Usuarioadmin)
admin.site.register(Mensagem, Mensagemadmin)