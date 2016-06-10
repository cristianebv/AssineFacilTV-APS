# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

ENUM_FORMA_PAG = (
 ('Cartao Debito', 'Cartao Debito'),
 ('Cartao Credito', 'Cartao Credito'),
)

ENUM_ESTADO = (
    ('Paraiba', 'Paraiba'),
    ('Pernambuco', 'Pernambuco'),
    ('Rio Grande do Norte', 'Rio Grande do Norte'),
    ('Ceara', 'Ceara'),
    ('Alagoas', 'Alagoas'),
    ('Sergipe', 'Sergipe'),
    ('Bahia', 'Bahia'),
    ('Piaui', 'Piaui'),
    ('Maranhao', 'Maranhao'),
)

class Endereco(models.Model):
	cep = models.CharField(max_length=9)
	rua = models.CharField(max_length=150)
	bairro = models.CharField(max_length=50)
	cidade = models.CharField(max_length=100)
	estado = models.CharField(max_length=50, choices=ENUM_ESTADO)

	def __unicode__(self):
		return self.rua

class Plano(models.Model):
	nome = models.CharField(max_length=150,
		verbose_name='Nome do Plano')
	valor = models.DecimalField(max_digits=6,decimal_places=2,
		verbose_name='Valor do Plano')	

	def __unicode__(self):
		return self.nome


class Cliente(models.Model):
	nome = models.CharField(max_length=100)
	cpf = models.CharField(max_length=14,
		verbose_name='CPF')
	email = models.EmailField(max_length=150)
	data_nascimento = models.DateField(blank=True, null = False,
		verbose_name='Data de Nascimento')
	nome_da_mae = models.CharField(max_length=150,
		verbose_name='Nome da Mãe')
	endereco = models.ForeignKey(Endereco,
		verbose_name='Endereço')
	plano = models.ForeignKey(Plano)

	def __unicode__(self):
		return self.nome

class Venda(models.Model):
	cliente = models.ForeignKey(Cliente)
	plano = models.ForeignKey(Plano)
	forma_pagamento = models.CharField(
		verbose_name='Forma de Pagamento', max_length=50 , choices = ENUM_FORMA_PAG)

	def __unicode__(self):
		return str(self.id)
		
