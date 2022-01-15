from django.contrib import admin
from .models import DiasVisita, Cidade, Imagem, Horario, Imoveis, Visitas

@admin.register(Imoveis)
class ImoveisAdmin(admin.ModelAdmin):
    list_display = ('rua', 'valor', 'quartos', 'tamanho', 'cidade', 'tipo')
    list_editable = ('valor', 'tipo')
    list_filter = ('cidade', 'tipo')

admin.site.register(DiasVisita)
admin.site.register(Cidade)
admin.site.register(Imagem)
admin.site.register(Horario)

admin.site.register(Visitas)