# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 06:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapa_app', '0017_auto_20170730_0135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abrirelaciona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataentrada', models.DateField()),
                ('codabrigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapa_app.Abrigo')),
            ],
            options={
                'verbose_name': 'Relaciona abrigo',
                'verbose_name_plural': 'Relaciona abrigos',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(blank=True, max_length=100, null=True, verbose_name='Produto')),
                ('quantidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='Quantidade')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.RemoveField(
            model_name='voluntario',
            name='quantidade',
        ),
        migrations.AddField(
            model_name='abrirelaciona',
            name='codusuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapa_app.Voluntario'),
        ),
    ]
