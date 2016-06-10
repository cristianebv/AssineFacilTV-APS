from django.contrib.admin import AdminSite
from AssineFacilTV.models import *
from django.utils.translation import ugettext_lazy
from django.contrib import admin

class AdminEndereco(admin.ModelAdmin):
	# Campos a serem exibidos na criacao de algum 
	fields = ('cep', 'rua', 'bairro', 'cidade', 'estado')

	# Colunas que devem aparecer
	list_display = ('Rua', 'Bairro', 'CEP', 'Cidade', 'Estado')

	""" Obtem as colunas para exibir no list_display """
	def Rua(self, obj):
		return obj.rua

	def Bairro(self, obj):
		return obj.bairro

	def CEP(self, obj):
		return obj.cep

	def Cidade(self, obj):
		return obj.cidade

	def Estado(self, obj):
		return obj.estado

	# Filtros a serem exibidos na esquerda
	list_filter = ('estado', 'cidade')

	# Define um campo de pesquisa que vai retornar resultados dos campos definidos abaixo
	search_fields = ['cep', 'rua', 'bairro', 'cidade', 'estado']

	# Quantidade de linhas a serem exibidas por pagina
	list_per_page = 10

	# Define que deve mostrar a quantidade total de resultados encontrados
	show_full_result_count = True

class AdminCliente(admin.ModelAdmin):
	# Campos a serem exibidos na criacao de algum 
	fields = ('nome', 'cpf', 'email', 'data_nascimento', 'nome_da_mae',
		'endereco', 'plano')

	# Colunas que devem aparecer
	list_display = ('Nome', 'CPF', 'Endereco', 'Email', 'Plano')

	""" Obtem as colunas para exibir no list_display """
	def Nome(self, obj):
		return obj.nome

	def CPF(self, obj):
		return obj.cpf

	def Endereco(self, obj):
		return obj.endereco.rua

	def Email(self, obj):
		return obj.email

	def Plano(self, obj):
		return obj.plano.nome

	# Filtros a serem exibidos na esquerda
	list_filter = ('endereco__estado', 'endereco__bairro', 'plano__nome')

	# Define um campo de pesquisa que vai retornar resultados dos campos definidos abaixo
	search_fields = ['nome', 'cpf', 'email', 'data_nascimento',
	'nome_da_mae', 'endereco__nome', 'plano__nome']

	# Quantidade de linhas a serem exibidas por pagina
	list_per_page = 10

	# Define que deve mostrar a quantidade total de resultados encontrados
	show_full_result_count = True

class AdminPlano(admin.ModelAdmin):
	# Campos a serem exibidos na criacao de algum 
	fields = ('nome', 'valor')

	# Colunas que devem aparecer
	list_display = ('Nome', 'Valor')

	""" Obtem as colunas para exibir no list_display """
	def Nome(self, obj):
		return obj.nome

	def Valor(self, obj):
		return obj.valor

	# Filtros a serem exibidos na esquerda
	list_filter = ('id', 'nome')

	# Define um campo de pesquisa que vai retornar resultados dos campos definidos abaixo
	search_fields = ['nome', 'id', 'valor']

	# Quantidade de linhas a serem exibidas por pagina
	list_per_page = 10

	# Define que deve mostrar a quantidade total de resultados encontrados
	show_full_result_count = True

class AdminVenda(admin.ModelAdmin):
	# Campos a serem exibidos na criacao de algum 
	fields = ('cliente', 'plano', 'forma_pagamento')

	# Colunas que devem aparecer
	list_display = ('Cliente_Nome', 'Plano_Nome', 'Forma_Pagamento')

	""" Obtem as colunas para exibir no list_display """
	def Cliente_Nome(self, obj):
		return obj.cliente.nome

	def Plano_Nome(self, obj):
		return obj.plano.nome

	def Forma_Pagamento(self, obj):
		return obj.forma_pagamento

	# Filtros a serem exibidos na esquerda
	list_filter = ('plano__nome', 'forma_pagamento')

	# Define um campo de pesquisa que vai retornar resultados dos campos definidos abaixo
	search_fields = ['cliente__nome', 'plano__nome', 'forma_pagamento']

	# Quantidade de linhas a serem exibidas por pagina
	list_per_page = 10

	# Define que deve mostrar a quantidade total de resultados encontrados
	show_full_result_count = True	


# Register your models here.
admin.site.register(Endereco, AdminEndereco)
admin.site.register(Cliente, AdminCliente)
admin.site.register(Plano, AdminPlano)
admin.site.register(Venda, AdminVenda)