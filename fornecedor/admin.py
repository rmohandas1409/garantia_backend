from django.contrib import admin
from fornecedor.models import Fornecedor

class Fornecedores(admin.ModelAdmin):
    list_display = ('id', 'razao_social', 'cpf_cnpj', 'inscricao', 'telefone', 'email')
    list_display_links = ('id', 'razao_social')
    search_fields = ('razao_social', 'cpf_cnpj',)
    list_per_page = 20

admin.site.register(Fornecedor, Fornecedores)