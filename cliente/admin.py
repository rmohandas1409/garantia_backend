from django.contrib import admin

from cliente.models import Cliente

class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
    ordering = ('nome',)

admin.site.register(Cliente, Clientes)
