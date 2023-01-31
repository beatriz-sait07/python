from django.contrib import admin
from core.models import Eventos

#enfeitando a visualização
class Evento_adm(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criação')
    list_filter = ('usuario','data_evento')

#registar class/models
admin.site.register(Eventos, Evento_adm)