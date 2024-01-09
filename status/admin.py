from django.contrib import admin

from status.models import Status

class Situacao(admin.ModelAdmin):
    list_display = ('id', 'descricao')
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao',)
    list_per_page = 20
    ordering = ('descricao',)

admin.site.register(Status, Situacao)
