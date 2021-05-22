from django.contrib import admin
from core.models import Licitacoes


class LicitacoesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Licitacoes, LicitacoesAdmin)
