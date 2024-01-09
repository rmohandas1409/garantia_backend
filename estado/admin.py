from django.contrib import admin

from estado.models import Estado

class Estados(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sigla')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
    ordering = ('nome',)

admin.site.register(Estado, Estados)
