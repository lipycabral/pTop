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
class AbrigoAdmin(admin.ModelAdmin):
    list_display = ['titulo','cep','espaco']
class CadastroAdmin(admin.ModelAdmin):
    list_display = ['nome']
class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ['volunt','cpf','cep','numero','ajuda']
class AbrigadoAdmin(admin.ModelAdmin):
    list_display = ['abrigado','necessidade','quantidade']
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['produto','quantidade']
class AbrirelacionaAdmin(admin.ModelAdmin):
    list_display = ['dataentrada',]

admin.site.register(Local, Localadmin)
admin.site.register(Abrirelaciona, AbrirelacionaAdmin)
admin.site.register(Cadastro, CadastroAdmin)
# admin.site.register(Usuario, Usuarioadmin)
admin.site.register(Mensagem, Mensagemadmin)
admin.site.register(Abrigo, AbrigoAdmin)
admin.site.register(Voluntario, VoluntarioAdmin)
admin.site.register(Abrigado, AbrigadoAdmin)
admin.site.register(Produto, ProdutoAdmin)