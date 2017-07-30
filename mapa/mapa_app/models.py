from django.contrib.auth.models import User
from django.db import models

# Create your models here.

CHOICE_ATD = (
    ('0', 'Não atendido'),
    ('1', 'Atendido'),
)

CHOICE_SN = (
    ('S', 'Sim'),
    ('N', 'Não'),
)

# class Pessoa(models.Model):
#     usuario = models.ForeignKey(User)
#     nome = models.CharField('Nome completo', max_length=100)
#     email = models.CharField('E-mail', max_length=100)
#     cpf = models.CharField('CPF', max_length=15)
#     senha = models.CharField('Senha', max_length=100)
#
#     class Meta:
#         verbose_name = 'Usuário'
#         verbose_name_plural = 'Usuários'
#     def __str__(self):
#         return '%s' % (self.nome,)

class Local(models.Model):
    #codusuario = models.ForeignKey(User)
    titulo = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.CharField(max_length=15, null=True, blank=True)
    altura = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'
    def __str__(self):
        return '%s' % (self.titulo,)

class Mensagem(models.Model):
    codchamado = models.ForeignKey(Local)
    datamensagem = models.DateField()
    mensagem = models.TextField('Mensagem', null=True, blank=True)
    resposta = models.CharField(u'Resposta', max_length=1, choices=CHOICE_ATD, default=0)
    class Meta:
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'
    def __str__(self):
        return '%s' % (self.mensagem,)
class Cadastro(models.Model):
    nome = models.CharField('Nome',max_length=100)
    senha = models.CharField('Senha', max_length=100)
    email = models.EmailField('Email', max_length=100)
    class Meta:
        verbose_name = 'Cadastro'
        verbose_name_plural = 'Cadastros'
    def __str__(self):
        return '%s' % (self.nome,)

