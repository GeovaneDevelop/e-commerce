# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 18:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em:')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em:')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Category')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
